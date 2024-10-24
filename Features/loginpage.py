from Locators import Locators_List
import logging
import os
from selenium import webdriver
import mysql.connector
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



current_directory = os.path.splitext(os.path.basename(__file__))[0]
logfile_name = f"{current_directory}.log"

# Set up logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(logfile_name),
        logging.StreamHandler()
    ]
)

def UserData_fromdatabase(userrole):
    try:
        Connection = None
        cursors = None
        dataload = None

        # DB Connection
        Connections = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vishal@123",
            database = "Test_Selenium"
        )
    

        if Connections.is_connected():
            logging.info("DB Connected successfully")
            cursors = Connections.cursor()
            cursors.execute('SELECT User_name, user_password from user_details where user_role = %s', (userrole,))

            row = cursors.fetchone()

            if row:
                user_name, password = row


            
    except Exception as e:
        logging.error(f'Error occured at establishing the db connection\n the error: {e}')       
    
    finally:
        if Connections:
            Connections.close()
        if cursors:
            cursors.close()
    return user_name, password      
    logging.info(f'The username: {user_name} and password: {password} from database')
    
    
# Login page functionality
def Partner_Login(username, password):
    
    # intilize driver
    global driver 
    driver = webdriver.Chrome()
    driver.maximize_window()

    logging.info("I launch chrome browser")

    # Open URL
    driver.get(Locators_List.URL)
    logging.info(f'Open {Locators_List.URL}')
    
    # Wait to page load and click on the login button
    Login_Button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.LoginButton_Xpath)))
    Login_Button.click()
    
    logging.info("Clicked on Login Button")
    

    # SignIn page
    Welcome_Message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.WelcomeMessage_Xpath)))
    logging.info(Welcome_Message.text)

    Input_EmailID = driver.find_element(By.XPATH, Locators_List.UserName_Xpath)
    Input_EmailID.send_keys(username)
    logging.info(f'I Entered the User Name: {username}')
    

    Input_Password = driver.find_element(By.XPATH, Locators_List.Password_Xpath)
    Input_Password.send_keys(password)
    logging.info(f'I Entered the Password: {password}')
    

    SignIn_Button = driver.find_element(By.XPATH, Locators_List.SignIn_Button)
    SignIn_Button.click()
    logging.info("Clicked on the login button")

    # Verify the user
    UserRole = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserRole_Xpath)))

    Role = UserRole.text

    if Role == "PARTNER":
        
        logging.info(f'Login Successful with the {Role}')
    else:
        logging.error('Login Failure!')

    time.sleep(10)
# Read user profile data
def ReadUserProfileData():

    UserButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserButton_Xpath)))
    UserButton.click()
    logging.info('I Clicked on the user')
    time.sleep(2)

    UserProfileButton = driver.find_element(By.XPATH, Locators_List.UserProfileButton_Xpath)
    UserProfileButton.click()
    logging.info('I Clicked on Profile')
    time.sleep(2)

    try:
        ProfileDataRowCount = driver.find_elements(By.XPATH, Locators_List.UserProfileDataRows_Xpath)
        row_count = len(ProfileDataRowCount)
        logging.info(f'count of rows:{row_count}')

        profile_data = {}

        for i in range(1, row_count+1):
            header = driver.find_element(By.XPATH, f"//div[@class='table-responsive']//table//tbody//tr[{i}]//th")
            header = header.text

            profiledata = driver.find_element(By.XPATH, f"//div[@class='table-responsive']//table//tbody//tr[{i}]//td" )
            data = profiledata.text

            profile_data[header] = data
    
        logging.info(profile_data)
        
    except Exception as e:
        logging.error(f'error occured at reading the data on profile pge\n Error: {e}')

    


    except Exception as e:

        logging.error(e)   
           
        

    time.sleep(5)

        
# Logout from the page
def Logout():

    UserButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators_List.UserButton_Xpath)))
    UserButton.click()
    logging.info('I Clicked on the User Botton')
    time.sleep(5)
    SignOutButton = driver.find_element(By.XPATH, Locators_List.SignOutButton_Button)
    SignOutButton.click()
    logging.info("Signout from the user")
    time.sleep(10)
    driver.close()
    logging.info('Close the browser')

user_name, password = UserData_fromdatabase("PARTNER")
Partner_Login(user_name, password)
ReadUserProfileData()
Logout()

