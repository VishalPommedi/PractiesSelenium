from selenium.webdriver.common.by import By
from behave import given, when, then
from behave import step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import logging
from log import LogConfigurator
import Orange_Hrm_locators
from commonsteps import capture_screenshot
import time
from RandomDetails import generate_employee_id
from selenium.webdriver.common.keys import Keys
emp_id = generate_employee_id()

Configurator = LogConfigurator()
@when(u'Navigate to the PIM page')
def navigate_to_pim(context):
    Configurator.beforeall(context)

    logging.info("Navigating to PIM page")
    wait = WebDriverWait(context.driver, 10)
    try:
        side_menu_options = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, Orange_Hrm_locators.sidemenu_xpath))
        )
        
        sidemenu_text = [i.text for i in side_menu_options]
        logging.info(f"Side menu options: {sidemenu_text}")
        # Check if PIM is in the side menu options
        PIM_option = next(i for i in side_menu_options if i.text == "PIM")
        if PIM_option:
            PIM_option.click()
            logging.info("Clicked on PIM option in side menu")
        else:
            logging.error("PIM option not found in side menu")
            capture_screenshot(context)
    except Exception as e:    
        logging.error(f"Error navigating to PIM page: {e}")
        capture_screenshot(context)
        context.driver.quit()
        
    
@then(u'goto the add employee tab')
def go_to_addemployee(context):
    Configurator.beforeall(context)
    try:
        wait = WebDriverWait(context.driver, 10)
        pim_option = wait.until(EC.presence_of_all_elements_located((By.XPATH, Orange_Hrm_locators.pim_topbar_options_xpath)))
        pim_option_text = [i.text for i in pim_option]
        logging.info(f"PIM top bar options: {pim_option_text}")

        Add_Employee = next(i for i in pim_option if i.text == "Add Employee") 
        Add_Employee.click()
        logging.info("Clicked on Add Employee option in PIM top bar")
        
        Add_Employee_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[.='Add Employee']")))
        if Add_Employee_text.text == "Add Employee":
            logging.info(Add_Employee_text.text)
        else:
            logging.warning("Add Employee page is not visible")
            capture_screenshot(context)
    except Exception as e:
        logging.error(f"Error navigating to Add Employee page: {e}")
        capture_screenshot(context)
        context.driver.quit()   


@then(u"create a new employee with login details")
def create_employee(context):
    Configurator.beforeall(context)

    try:
        time.sleep(5)
        logging.info("*Create a new employee with login details")
        wait = WebDriverWait(context.driver, 10)
        firstName_textbox = wait.until(EC.presence_of_element_located((By.XPATH, Orange_Hrm_locators.firstName_xpath)))
        middleName_textbox = context.driver.find_element(By.XPATH, Orange_Hrm_locators.middleName_xpath)
        lastName_textbox = context.driver.find_element(By.XPATH, Orange_Hrm_locators.lastName_xpath)

        firstName_textbox.send_keys("Vishal")
        time.sleep(1)
        middleName_textbox.send_keys("Kumar")
        time.sleep(1)
        lastName_textbox.send_keys("Pommedi")
        time.sleep(1)
        employee_id_textbox = wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Hrm_locators.employeeId_xpath)))
        employee_id_textbox.send_keys(Keys.CONTROL, "a")
        employee_id_textbox.send_keys(Keys.DELETE)
        time.sleep(2)
        employee_id_textbox.clear()
        time.sleep(1)
        employee_id_textbox.send_keys(emp_id)# emp_id from the RandomDetails module

        create_login_with_details_toggle = context.driver.find_element(By.XPATH, Orange_Hrm_locators.create_login_switch_xpath)

        if create_login_with_details_toggle.is_selected():
            logging.info("the toggle is enabled")
        else:
            logging.info("the toggle is disabled")

        save_button = context.driver.find_element(By.XPATH, Orange_Hrm_locators.save_button_xpath)
        save_button.click()

        toast_head = wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Hrm_locators.toast_head))).text
        toast_message = context.driver.find_element(By.XPATH, Orange_Hrm_locators.toast_message).text
        logging.info(f"The toast head message: {toast_head}")
        logging.info(f"The toast message: {toast_message}")


        time.sleep(10)


    except Exception as e:
        logging.error(f"The error occured in create new employee with login details method. The error: {e}")

@then(u'verify the employee is created successfully')
def toast_message(context):
    try:
        Configurator.beforeall(context)
        wait = WebDriverWait(context.driver, 10)
        toast_head = wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Hrm_locators.toast_head))).text
        toast_message = context.driver.find_element(By.XPATH, Orange_Hrm_locators.toast_message).text

        if toast_head == "Success":

            logging.info(f"The toast head message: {toast_head}")
            logging.info(f"The toast message: {toast_message}")
        else:
            capture_screenshot(context)
            logging.warning("Failed to create the new user!")   
    except Exception as e:
        logging.error(f"The error occured at verify the employee created successfully: {e}")  
        capture_screenshot(context)
        context.driver.quit()

