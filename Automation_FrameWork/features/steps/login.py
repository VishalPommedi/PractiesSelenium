import time
import random
import string
import Locators
import logging
from commonsteps import RepeatSteps
from log import LogConfigurator
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

Configurator = LogConfigurator()

@given(u'I launch the Chrome Browser')
def OPen_Browser(context):
    # context.driver
    pass

@when(u'I Navigated to the Pega Login page')
def OpenUrl(context):

    Configurator.beforeall(context)

    try:
        context.driver.get(Locators.WebSite_URL)
        # print(f'Navigated to the website: {Locators.WebSite_URL}')
        logging.info(f'navigated to the website: {Locators.WebSite_URL}')

    except Exception as e:
        # print(f'Erorr occureted at navigete to the url. Error: {e}')
        logging.error(f'Erorr occureted at navigete to the url. Error: {e}')

@then(u'I Entered "{UserName}" and "{Password}"')
def step_impl(context, UserName, Password):
    Configurator.beforeall(context)
    User_Name = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.user_name_xpath)))
    PassWord = context.driver.find_element(By.XPATH, Locators.password_xpath)

    random_userName = "".join(random.choices(string.ascii_lowercase, k=5))

    User_Name.send_keys(random_userName)
    time.sleep(1)
    PassWord.send_keys(Password)
    time.sleep(1)

    logging.info(f'The user name and password is: {UserName}, {Password} ')


@when(u'User Login Successfully verify the user Name')
def step_impl(context):

    Configurator.beforeall(context)

    SignIn_Button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.SignInButton_xpath)))
    SignIn_Button.click()

    logging.info('Clicked on the Signin Button')

    # Verify the Home Screen
    HomeScreen_Message = context.driver.find_element(By.XPATH, Locators.HomeScreen_Text_xpath)
    if Locators.ExpectedHomeScreen_text == HomeScreen_Message.text:
        # print('Login Successful')
        logging.info('Login Success')
    else:
        # print('Login Failure!')
        logging.warning('Login Failure')


 
@then(u'Close the Browser')
def step_impl(context):
   pass

@then(u'Logout')
def LogOut(context):
    try:
        Configurator.beforeall(context)
        SelectOption = RepeatSteps()
        Option = "Sign Out"
        SelectOption.SelectOption_from_GearIcon(context, Option)
        logging.info('Clicked on the "Sign Out" Button')
        time.sleep(5)
    except Exception as e:
        logging.error(f'The error occured at click on Sign Out Button. The error: {e}')

@when(u'Nivaigate to the Home page')
def navigate_to_homepage(context):
    wait = WebDriverWait(context.driver, 10)
    Configurator.beforeall(context)

    try:
        Home_link = context.driver.find_element(By.XPATH, Locators.home_link_xpath)
        Home_link.click()
        logging.info("Navigated to the home page")

    except Exception as e:

        logging.error(f"The error occured while navigating the home page. The error: {e}")            