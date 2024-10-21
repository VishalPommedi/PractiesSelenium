from Locators import Locators_List
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Login page functionality
def Partner_Login():
    
    # intilize driver
    global driver 
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

    # Verify the user
    UserRole = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserRole_Xpath)))

    Role = UserRole.text

    if Role == "PARTNER":
        print(f'Login Successful with the {Role}')
    else:
        print(f'Login Failure!')

    time.sleep(10)
# Read user profile data
def ReadUserProfileData():

    UserButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserButton_Xpath)))
    UserButton.click()
    print('Clicked on the User Button')
    time.sleep(2)

    UserProfileButton = driver.find_element(By.XPATH, Locators_List.UserProfileButton_Xpath)
    UserProfileButton.click()
    print('clicked on the user profile')
    time.sleep(2)

    ProfileDataRowCount = driver.find_elements(By.XPATH, Locators_List.UserProfileDataRows_Xpath)
    row_count = len(ProfileDataRowCount)
    print(f'count of rows:{row_count}')
    # for row in range(row_count):
    time.sleep(5)

        
# Logout from the page
def Logout():

    UserButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserButton_Xpath)))
    UserButton.click()
    print('Clicked on the User Button')
    time.sleep(5)
    SignOutButton = driver.find_element(By.XPATH, Locators_List.SignOutButton_Button)
    SignOutButton.click()
    print('signout from the user')
    time.sleep(10)
    driver.close()
    print('close the browser')


Partner_Login()
ReadUserProfileData()
Logout()