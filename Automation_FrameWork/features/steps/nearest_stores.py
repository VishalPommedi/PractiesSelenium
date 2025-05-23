import time
import Locators
import logging
from behave import *
from selenium import webdriver
from log import LogConfigurator
from commonsteps import RepeatSteps
from commonsteps import capture_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

obj = RepeatSteps()
Configurator = LogConfigurator()

@then(u'Click on the stores Button')
def clickOn_Button(context):
    Configurator.beforeall(context)
    wait = WebDriverWait(context.driver, 10)

    try:
        button_name = "Stores"
        obj.Select_button(context, button_name)
        
    
        # verify the use is navigated to the stores page
        stored_head = wait.until(EC.presence_of_element_located((By.XPATH, Locators.stores_head_xpath)))
        logging.info("Clicked on the Stores button")
        if stored_head.text == Locators.stores_head_text:
            logging.info("Successfully navigated to the Stores page!")
            capture_screenshot(context)
            
        else:
            logging.warning("Failed to navigated the stores page")
            capture_screenshot(context)
            
    except Exception as e:
        logging.ERROR(f"The error occured at navigate the the stores page. The issue: {e}")     
        capture_screenshot(context)
        context.driver.quit()   

@then(u'Enter the "{Zip_Number}" then click on "FInd Store" Button')
def enter_data(context, Zip_Number):
    Configurator.beforeall(context)
    wait = WebDriverWait(context.driver, 10)
    try:
        ZipCode_input = context.driver.find_element(By.XPATH, Locators.zipCode_input_xpath)
        ZipCode_input.send_keys(Zip_Number)
        logging.info(f"Entered the zip number: {Zip_Number}")
        time.sleep(1)

        findStore_button = context.driver.find_element(By.XPATH, Locators.findStore_button)
        findStore_button.click()
        logging.info("clicked on the find stores button")
        time.sleep(15)

    except Exception as e:
        logging.error(f"The error occured the enter the zip code method. the error: {e}")


@then(u'read the store address')
def read_store_address(context):
    wait = WebDriverWait(context.driver, 10)
    Configurator.beforeall(context)

    try:
        Store_data = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.nearestStore_data_xpath)))
        Store_address = [adrs.text for adrs in Store_data]
        logging.info(f"The store address is: {Store_address}")

    except Exception as e:
        logging.error(f"The error occured at the read the nearest store data: {Store_address}")

