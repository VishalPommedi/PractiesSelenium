import time
import os
import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
from log import LogConfigurator

Configurator = LogConfigurator()

class RepeatSteps:
    
    def SelectOption_from_GearIcon(self, context, option):
        try:
            wait = WebDriverWait(context.driver, 10)
            Action = ActionChains(context.driver)
            # Hover over on the gear icon
            Gear_Icon = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.GearIcon_xpath)))
            Action.move_to_element(Gear_Icon).perform()

            Icons_Under_Gear = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.Profile_Details_xpath)))
        
            Selected_Option = next((i for i in Icons_Under_Gear if i.text == option), None)
        

            if Selected_Option is None:
                raise Exception('The customer button is not found under the Gear Icon')
                    
            Selected_Option.click()
        except Exception as e:
            print(f'The error is occurred  at selecting the {option}. The error: {e}')

    def Switch_Window(self, context):
        Current_Window = context.driver.current_window_handle
        WebDriverWait(context.driver, 10).until(lambda d: len(context.driver.window_handles)>1)

        new_window = [window for window in context.driver.window_handles if window != Current_Window][0]

        context.driver.switch_to.window(new_window)
        time.sleep(3)

        return new_window
    
    # below method is used to select one option from the list (Pega)
    def Select_button(self, context, button_name):
        wait = WebDriverWait(context.driver, 10)
        all_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.Menu_Options_xpath)))
        selected_button = next(button for button in all_buttons if button.text == button_name)
        selected_button.click()


def capture_screenshot(context):
    Configurator.beforeall(context)
    try:
        # Get the full path to the current feature file
        feature_path = context.feature.filename
        
        # Extract directory and feature name
        feature_dir = os.path.dirname(feature_path)
        feature_name = os.path.splitext(os.path.basename(feature_path))[0]

        # Screenshot name (overwrite each time)
        screenshot_path = os.path.join(feature_dir, f"{feature_name}.png")

        # Take screenshot
        context.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {e}")
