import time
from behave import *
import logging
import Locators
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from log import LogConfigurator
from selenium.webdriver.common.action_chains import ActionChains
from commonsteps import RepeatSteps
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Configurator = LogConfigurator()
Step = RepeatSteps()


@then(u'Select Finance under the Gear Icon')
def SelectFinance(context):
    Configurator.beforeall(context)
    step = RepeatSteps()
    Option = "Finance"
    step.SelectOption_from_GearIcon(context, Option)
    Configurator.beforeall(context)
    logging.info(f"Selected the {Option} from the Gear Icon")

    # Switch to new window
    Step.Switch_Window(context)

    


@then(u'Enter the Finance User name and Password and login')
def financeLogin(context):
    try:
        UserName = "Finance"
        Password = "Test@1234"
        User_Name = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.user_name_xpath)))
        PassWord = context.driver.find_element(By.XPATH, Locators.password_xpath)

        User_Name.send_keys(UserName)
        time.sleep(1)
        PassWord.send_keys(Password)
        time.sleep(1)

        logging.info(f'The user name and password is: {UserName}, {Password} ')

        # Click on Sign In button
        SignIn_Button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.SignInButton_xpath)))
        SignIn_Button.click()

        logging.info('Clicked on the Signin Button')
        time.sleep(2)

    except Exception as e:
        logging.error(f'The error is occured at login as finance head. The error: {e}')
        print(e)

@when(u'Naviagated to the Finance Home page')
def verifyFinanceLogin(context):
    Configurator.beforeall(context)
    Action = ActionChains(context.driver)
    try:
        logging.info('$$$$$$$$$$$$$$$$$$$ - Hover over on Gear Icon - $$$$$$$$$$$$$$$$$$$')
        FinanceHome = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.F_HomePage_xpath)))
        logging.info(FinanceHome.text)
        time.sleep(1)

    except Exception as e:
        logging.error(e)
        logging.error('The error occred at selecting the Del Chgs from gear icon')

            

@then(u'Select Del Chgs and Accept it')
def Select_DelChanges(context):

        try:
            Configurator.beforeall(context)
            Action = ActionChains(context.driver)
            logging.info('$$$$$$$$$$$$$$$$$$$ - Hover over on Gear Icon - $$$$$$$$$$$$$$$$$$$')
            F_GearIcon = context.driver.find_element(By.XPATH, Locators.F_GearIcon_xpath)

            Action.move_to_element(F_GearIcon).perform()

            allOptions = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, Locators.F_GearOptions_xpath)))
    
            DelChgs = next((i for i in allOptions if i.text == "Del Chgs"), None)

            if DelChgs:
                logging.info(f'The {DelChgs.text} is found')
                DelChgs.click()

                try:
                    logging.info("$$$$$$$$$$$$$$$$$$$ - Allert - $$$$$$$$$$$$$$$$$$$")
                    # alert = context.driver.switch_to.alert
                    # logging.info(f'The alert text is: {alert.text}')

                    # alert.dismiss()  
                    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
                    alert = Alert(context.driver)
                    alert_text = alert.text
                    logging.info(f'The alert text is: {alert_text}')
                    alert.accept()
                except Exception as e:
                    logging.error(f'The error occured at dismiss the pop-up. The error is: {e}')
            else:
                logging.error(f'The {DelChgs.text} is not found!')
            logging.info('Clicked on the ', DelChgs.text) 
            time.sleep(1)
    
        except Exception as e:
             logging.error(f'The error occured at click on the {DelChgs.text}. The error is: {e}')
              
        time.sleep(2)

@then(u'Close the tab')
def Close_Current_tab(context):

    logging.info('############## Close the current tab ##############')
    context.driver.close()

