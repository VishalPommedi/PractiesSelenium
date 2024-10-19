from Locators import Locators_List
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Partner_Login():
    
    # intilize driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    print('Launch Chrome Browser')

    # Open URL
    driver.get(Locators_List.URL)

    print(f'Open {Locators_List.URL}')
    
    # Wait to page load and click on the login button
    Login_Button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.LoginButton_Xpath)))
    Login_Button.click()
    print('Clicked on Login Button')
    

    # SignIn page
    Welcome_Message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.WelcomeMessage_Xpath)))
    print(Welcome_Message.text)

    Input_EmailID = driver.find_element(By.XPATH, Locators_List.UserName_Xpath)
    Input_EmailID.send_keys(Locators_List.Partner_Username)
    print(f'Enter User Name: {Locators_List.Partner_Username}')

    Input_Password = driver.find_element(By.XPATH, Locators_List.Password_Xpath)
    Input_Password.send_keys(Locators_List.Password)
    print(f'Enter Password: {Locators_List.Password}')

    SignIn_Button = driver.find_element(By.XPATH, Locators_List.SignIn_Button)
    SignIn_Button.click()
    print(f'Clicked on the login button')

    time.sleep(10)


Partner_Login()