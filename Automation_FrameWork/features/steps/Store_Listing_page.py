import time
import logging
import Locators
from behave import *
from selenium import webdriver
from log import LogConfigurator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Configurator = LogConfigurator()

@then(u'Navigate to "Store Listing" page')
def Navigate_StoreListingpage(context):
    time.sleep(1)
    Action = ActionChains(context.driver)
    Configurator.beforeall(context)
    logging.info('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Navigate to the "Store Listing" page $$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    wait = WebDriverWait(context.driver, 10)


    Menu = wait.until(EC.visibility_of_all_elements_located((By.XPATH, Locators.Menu_Options_xpath)))

    Menu_Options = [i.text for i in Menu]

    logging.info(f'The Menu Options are: {Menu_Options}')

    try:
        

        Stores_Button = next((i for i in Menu if i.text == "Stores"), None)

        if Stores_Button:
            logging.info('The menu option is found on the Menu options')
            Action.move_to_element(Stores_Button).perform()
            time.sleep(1)
        else:
            logging.error('The Store button is not found in the menu options')
    except Exception as e:
        logging.error(f'The error occured at hover over on the stores menu option, the error {e}')        

    logging.info('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Navigated to the "Store Listing" page $$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    StoreListing_Button = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.Stores_StoreListing_xpath)))

    StoreListing_Button.click()

    time.sleep(2)

    try:


        StoreListingText = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.StoerListing_Text_xpath)))

        if StoreListingText.text == "Store Listing":
            logging.info('Successfully Navigated to the Store listing page')
        else:
            logging.error('Failed to Navigate store listing page')

        time.sleep(2)
    except Exception as e:
        logging.error('The error occured at Navigate to Stores Listing page')
    time.sleep(2)        

@then(u'read the data')
def Read_Data(context):
    Table_Rows = context.driver.find_elements(By.XPATH, Locators.StoreListening_TableRows_xpath)
    RowsCount = len(Table_Rows)
    logging.info(f'Rows:{RowsCount}')

    data = []
    for i in range(2, RowsCount+1):
        sub_data = []
        Row_Columns = context.driver.find_elements(By.XPATH, f"//table[@id='search_store_list']//tbody//tr[{i}]//td")
        
        for td in Row_Columns:
            sub_data.append(td.text)

        data.append(sub_data)

    logging.info(data)    
    Configurator.after(context)