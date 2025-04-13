import time
from behave import *
import logging
import random
import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from log import LogConfigurator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Configurator = LogConfigurator()

@then(u'Select the shipping company, save the company title, and get back to the first window')
def Shipping_company(context):

    time.sleep(2)
    try:

        action_chain = ActionChains(context.driver)

        Menu_Options = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="menu"]//ul//li//a[@class="menu_option"]')))
        Menu_Options_text = [i.text for i in Menu_Options]
        logging.info(f'Menu Options: {Menu_Options_text}')

        for i in Menu_Options:
            if i.text == "Shipping":
                action_chain.move_to_element(i).perform()
                element_underShipping_xpath = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, Locators.shppingSubMenu_xpath)))
                shpping_options = [i.text for i in element_underShipping_xpath]
                logging.info(f'Shipping options: {shpping_options}')

                random_option = random.choice(element_underShipping_xpath)
                random_option.click()
                logging.info(f'Selected option: {random_option.text}')
                
        current_window = context.driver.current_window_handle
        logging.info(f'Current window Handle: {current_window}')
                
        WebDriverWait(context.driver, 10).until(EC.number_of_windows_to_be(2))
        logging.info("* For loop start to read the title of opened web page.")
        for window_handle in context.driver.window_handles:
            logging.info("In for loop")
            if window_handle != current_window:
                    logging.info("In If condition", window_handle)
                    context.driver.switch_to.window(window_handle)
                    logging.info(f'Web page name is: {context.driver.title}, and close')
                    context.driver.close()  
                    context.driver.switch_to.window(current_window) 
                    logging.info("Switching back to first window")            
                         
    except Exception as e:
        logging.error(f'The error occured at Shipping_company method. The error: {e}')       



