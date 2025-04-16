import time
from Orange_Hrm_locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
import logging
from log import LogConfigurator
from commonsteps import *

Configurator = LogConfigurator()

@Given("Launch the broser")
def orh_launch_browser(context):
    # try:
    #     context.driver = webdriver.Chrome()
    #     context.driver.maximize_window()
        
    # except Exception as e:
    #     print("The error occured at orh_launch_broswe method. the error: ", e)
    pass

@when("Open the Orange HRM webapp")
def orh_open_url(context):
    Configurator.beforeall(context)
    try:
        
        wait = WebDriverWait(context.driver, 10)
        context.driver.get(orangehrm_url)
        login_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h5[normalize-space()='Login']")))

        if login_text:
            logging.info(login_text.text)
        else:
            logging.warning("Login page is not visible")
    except Exception as e:
        logging.error("The error occuredt at orh_open_url method. The error: ", e)  

@then("Login with user name, and password")
def orh_enter_uname_pass(context):
    Configurator.beforeall(context)
    try:
        userName = context.driver.find_element(By.XPATH, username_textbox_xpath)
        password = context.driver.find_element(By.XPATH, password_textbox_xpath)
        loging_button = context.driver.find_element(By.XPATH, Login_button_xpath)

        userName.send_keys(orh_admin_u)
        time.sleep(1)
        password.send_keys(orh_admin_p)
        time.sleep(1)
        logging.info(f"login with username: {orh_admin_u} and password: {orh_admin_p}")
        loging_button.click()
        
    except Exception as e:  
        capture_screenshot(context) 
        logging.error("The error occured at orh_enter_uname_pass method. the error: ", e) 

@then("Naviate to the profile options and click on the About button")
def orh_click_about_button(context):

    Configurator.beforeall(context)
    try:
        wait = WebDriverWait(context.driver, 10)

        profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, userprofile_xpath)))
        profile_button.click()

        profile_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, profile_options_xpath)))
        profile_options_text = [i.text for i in profile_options]
        
        logging.info(f"Profile options: {profile_options_text}")

        About_button = next((i for i in profile_options if i.text == "About"), None)

        if About_button:
            About_button.click()
            
        else:
            logging.warning("About button not found!!")
        capture_screenshot(context)    


    except Exception as e:  
        logging.error(f"The error occured at orh_read_profile_data method. the error: {e}")  

@then("Read the user data")
def orh_read_profile_data(context):
    Configurator.beforeall(context)
    try:

        wait = WebDriverWait(context.driver, 10)
        About_on_popup = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='About']")))
        print("**", About_on_popup.text)
        time.sleep(5)
        
        time.sleep(10)

        user_about_details = context.driver.find_elements(By.XPATH, aboutpage_all_details_xpath)

        text_list = [i.text.strip() for i in user_about_details]

        info_dict = {}

        print("** Raw data: ",text_list)
        for i in range(0, len(text_list), 2):
            key = text_list[i].replace(":", "")
            value = text_list[i+1]
            info_dict[key] = value
        logging.info(f'user details: {info_dict}')
        time.sleep(2)
        close_button = context.driver.find_element(By.XPATH, aboutpage_close_button_xpath)
        close_button.click()
    except Exception as e:
        print("The error from the orh_read_profile_data. The error is: ", e)
        logging.error(f"The error from the orh_read_profile_data. The error is: {e}")

@then("Logout from page")
def orh_logout(context):
    try:
        Configurator.beforeall(context)
        wait = WebDriverWait(context.driver, 10)
        profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, userprofile_xpath)))
        profile_button.click()
        time.sleep(5)

        profile_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, profile_options_xpath)))
        profile_options_text = [i.text for i in profile_options]
        logging.info(f"The profile optins: {profile_options_text}")

        logout_button = next((i for i in profile_options if i.text == "Logout"), None)

        if logout_button:
            logout_button.click()
            time.sleep(5)
            
        else:
            logging.warning("** unable to click on the logout button!!")



    except Exception as e:
        logging.error(f'The error occured at orh_logout method. The error: {e}')

@then("close the web browser")
def orh_close_browser(context):
    # try:
    #     if context.driver:
    #         context.driver.close()
    #     else:
    #         print("Unable to close the browser")
    # except Exception as e:
    #     print(e, "close browser") 
    pass       