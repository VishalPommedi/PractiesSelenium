import time
import Locators
from RandomDetails import Random_names
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

FirstName, LastName, Email, CC_Num, Zip_code, Mobile_no, Area_code, company_name = Random_names()

@when(u'Click on the Cart Button')
def ClickOn_Curt(context):
    time.sleep(1)
    try:
        Cart_Button = context.driver.find_element(By.XPATH, Locators.CartImage_xpath)
        Cart_Button.click()
        print('Clicked on the "Cart Button"')
        

    except Exception as e:
        print('Error: ',e)
        print('the error occured at click on the "Cart Button"')
    time.sleep(2)
@then(u'Click on the Next Button')
def ClickOn_Next_Button(context):
    try:
        while True:
            try:
                NextButton = WebDriverWait(context.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, Locators.NextButton_xpath))
                )

                if NextButton.is_displayed():
                    print('The Next Button is visible on the screen')
                    break
            except Exception:
                pass
            context.driver.executive_script("window.scrollby(0, 500);")
            
        NextButton.click()
        print('clicked on the next button')

    except Exception as e:
        print('Error occured at click on the "Next" Button')

    time.sleep(5)

@then(u'Add Billing addres Details, select Shipping to Billing addres')
def AddTheBilling_Address(context):
    print('***************Adding Billing details****************')
    try:
        First_Name = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.FirstName_xpath))
        )    

        First_Name.send_keys(FirstName)
        print(f'First Name: {FirstName}')
        time.sleep(1)

        Last_Name = context.driver.find_element(By.XPATH, Locators.LastName_xapth)
        Last_Name.send_keys(LastName)
        print(f'Last Name: {LastName}')
        time.sleep(1)

        CompanyName = context.driver.find_element(By.XPATH, Locators.CompanyName_xapth)
        CompanyName.send_keys(company_name)
        print(f'Last Name: {company_name}')
        time.sleep(1)

        StreetAddress = context.driver.find_element(By.XPATH, Locators.StreetAddress_xpath)
        StreetAddress.send_keys("4-29/1 Down Town")
        print('4-29/1 Down Town')
        time.sleep(1)

        ZipCode =  context.driver.find_element(By.XPATH, Locators.ZipCode_xapth)
        ZipCode.send_keys(Zip_code)
        print(f'Zip Code: {Zip_code}')
        time.sleep(1)

        AreaCode =  context.driver.find_element(By.XPATH, Locators.AreaCode_xapth)
        AreaCode.send_keys(Area_code)
        print(f'Area Code: {Area_code}')
        time.sleep(1)

        Primary_Phone = context.driver.find_element(By.XPATH, Locators.PrimaryPhoneNumber_xapth)
        Primary_Phone.send_keys(Mobile_no)
        print(f'Primary Phone Number: {Mobile_no}')
        time.sleep(1)

        # Click on the Shipping to Billing Address
        ShippingToBillingAddress = context.driver.find_element(By.XPATH, Locators.ShipToBillingAddress_xpath)
        ShippingToBillingAddress.click()

        #Click on the Next Button
        NextButton = context.driver.find_element(By.XPATH, Locators.NextButton_xpath)
        NextButton.click()



    except Exception as e:
        print('The error occured at to enter billing details')
        print(e)
    time.sleep(15)