import time
import os
from selenium import webdriver
from RandomDetails import Random_Details
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from Log_config import setup_logger

'''
In this file I am going to register a user on demo website and Login with the new credentials
'''

log = setup_logger()

script_name = os.path.splitext(os.path.basename(__file__))[0]
screenshot_name = f"{script_name}.png"

script_dir = os.path.dirname(os.path.abspath(__file__))
screenshot_path = os.path.join(script_dir, screenshot_name)

WebSite_URL = "https://demowebshop.tricentis.com/"

FirstName, LastName, EmailID = Random_Details()
Password = "Test@12345"


def RegisterUser():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(WebSite_URL)

    logo = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.XPATH, "//div[@class='header-logo']")))
    print(f'Navigated to the website: {WebSite_URL}')
    log.info(f'The web site: {WebSite_URL}')

    # Navigate to Registration page
    Headers_LinkWrapper = driver.find_elements(By.XPATH, "//div[@class='header-links-wrapper']//div//ul//li")

    List_Of_Data = [i.text for i in Headers_LinkWrapper]
    print(List_Of_Data)

    for i in Headers_LinkWrapper:
        if i.text == "Register":
            i.click()
            print('clicked on the Registration link')
            break

    # Register a user
    Registration_page = WebDriverWait(driver, 10).until(Ec.presence_of_element_located, ((By.XPATH, "//div[@class='page registration-page']//h1")))   

    Gender_Male = driver.find_element(By.ID, "gender-male")
    Gender_Male.click()

    if Gender_Male.is_selected:
        print(f'{Gender_Male.text}Gender selected')
    else:
        print('Gender not selected')

    

    try:
        First_Name = driver.find_element(By.ID, "FirstName")
        First_Name.send_keys(FirstName)
        print(f'First Name: {FirstName}')
        time.sleep(1)
        Last_Name = driver.find_element(By.NAME, "LastName")
        Last_Name.send_keys(LastName)
        print(f'Last Name: {LastName}')
        time.sleep(1)
        Email_id = driver.find_element(By.NAME, "Email") 
        Email_id.send_keys(EmailID)
        print(f'Email ID: {EmailID}') 
        time.sleep(2)

        user_password = driver.find_element(By.XPATH, "//input[@id='Password']")
        user_password.send_keys('Test@12345')
        time.sleep(1)
        Re_enter_password = driver.find_element(By.ID, "ConfirmPassword")
        Re_enter_password.send_keys(Password)
        time.sleep(1)
        print(f'Password: {Password}')

        Register_Button = driver.find_element(By.XPATH, "//input[@id='register-button']")
        Register_Button.click()        
    except Exception as e:
        print(f'error occured adding user details. The error: {e}')


    try:

        result = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.XPATH, "//div[@class='result']")))  

        if result.text == "Your registration completed":
            print(result.text)
            time.sleep(3)
            continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
            continue_button.click()
        else:
            print('Registraion got failed')

    except Exception as e:
        print('error occured at verify registration')        
    time.sleep(3)
    # Logout from the page
    try:
        Logout = driver.find_element(By.XPATH, "//a[normalize-space()='Log out']")
        Logout.click()

    except Exception as e:
        print(f'error occured at to logout from the page. error: {e}')  
  
   
    

    try: 
        # Re login to web site with registered details
        Login = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
        Login.click()
    except Exception as e:
        print(e)    

        driver.save_screenshot(screenshot_path)

    try:
    # Login 
        email_id = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.XPATH, "//input[@class='email']")))
        email_id.send_keys(EmailID)
        time.sleep(2)

        password_textbox = driver.find_element(By.ID, "Password")
        password_textbox.send_keys(Password)
        time.sleep(1)
        remember_me_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        remember_me_checkbox.click()
        time.sleep(1)
        Login_Button_1 = driver.find_element(By.XPATH, "//input[@value='Log in']")
        Login_Button_1.click()

    except Exception as e:
            print(e)

    time.sleep(15)   


RegisterUser()    