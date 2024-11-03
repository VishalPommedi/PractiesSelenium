import time
import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given(u'I launch the Chrome Browser')
def OPen_Browser(context):
    # context.driver
    pass

@when(u'I Navigated to the Pega Login page')
def OpenUrl(context):
    try:
        context.driver.get(Locators.WebSite_URL)
        print(f'Navigated to the website: {Locators.WebSite_URL}')

    except Exception as e:
        print(f'Erorr occureted at navigete to the url. Error: {e}')

@then(u'I Entered "{UserName}" and "{Password}"')
def step_impl(context, UserName, Password):
    User_Name = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.user_name_xpath)))
    PassWord = context.driver.find_element(By.XPATH, Locators.password_xpath)

    User_Name.send_keys(UserName)
    time.sleep(1)
    PassWord.send_keys(Password)
    time.sleep(1)


@when(u'User Login Successfully verify the user Name')
def step_impl(context):
    SignIn_Button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.SignInButton_xpath)))
    SignIn_Button.click()

    # Verify the Home Screen
    HomeScreen_Message = context.driver.find_element(By.XPATH, Locators.HomeScreen_Text_xpath)
    if Locators.ExpectedHomeScreen_text == HomeScreen_Message.text:
        print('Login Successful')
    else:
        print('Login Failure!')

@then(u'Logout')
def step_impl(context):
    try:
        # initializing the ActionChains with driver
        action = ActionChains(context.driver)

        Gear_Icon = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.GearIcon_xpath)))

        action.move_to_element(Gear_Icon).perform()
        time.sleep(5)
        Profile_Options = context.driver.find_elements(By.XPATH, Locators.Profile_Details_xpath)

        All_Options = [i for i in Profile_Options]
        OPtion_Names = [i.text for i in Profile_Options]
        print(f'Profile Options: {OPtion_Names}')

        for option in All_Options:
            if option.text == "Sign Out":
                option.click()
                print(f'clicked on the {option.text}')
                break
        time.sleep(10)    
    except Exception as e:
        print(f'error: {e}. The error occured while performing the Signout operation')



@then(u'Close the Browser')
def step_impl(context):
   pass