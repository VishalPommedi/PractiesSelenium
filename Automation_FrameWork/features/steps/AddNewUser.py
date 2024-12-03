import time
import random
import Locators
from behave import *
from RandomDetails import Random_names
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FirstName, LastName, Email, CC_Num, Zip_code, Mobile_no, Area_code, company_name = Random_names()


@then(u'Navigate to customer page')
def Navigate_to_Customer_Page(context):
    wait = WebDriverWait(context.driver, 10)
    Action = ActionChains(context.driver)

    try:
        # Hover over on the gear icon
        Gear_Icon = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.GearIcon_xpath)))
        Action.move_to_element(Gear_Icon).perform()

        Icons_Under_Gear = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.Profile_Details_xpath)))
        
        Customers_Button = next((i for i in Icons_Under_Gear if i.text == "Customers"), None)
        

        if Customers_Button is None:
            raise Exception('The customer button is not found under the Gear Icon')
                    
        Customers_Button.click()
    except Exception as e:
        print('the error occured at navigate to the customer page')
        raise        
    time.sleep(2)

@then(u'Add Customer details "Account Number", "Customer Name", "Company Name", and click on "Add Customer button"')
def addCustomer_details(context):
    wait = WebDriverWait(context.driver, 10)
    try:

        accountNumber = wait.until(EC.presence_of_element_located((By.XPATH, Locators.Accountnumber_input_xpath)))
        accountNumber.send_keys(CC_Num)
        print('Account Number: ', CC_Num)
        time.sleep(1)

        customerName = context.driver.find_element(By.XPATH, Locators.Customername_input_xpath)
        customerName.send_keys(FirstName)
        print('Customer name: ', FirstName)
        time.sleep(1)

        companyName = context.driver.find_element(By.XPATH, Locators.Companyname_input_xpath)
        companyName.send_keys(company_name)
        print('Company name: ', company_name)
        time.sleep(1)

        addCustomer_Button = context.driver.find_element(By.XPATH, Locators.Addcustomer_Button_xpath)
        addCustomer_Button.click()
       

    except Exception as e:
        print('The error occured at saving the user basic details: ', e)

    time.sleep(2)  

# Navigated to the "New Customer page"
@when(u'Navigated to the "New Customer page"')
def verifyNewCuustomerPage(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        # verify that user navigated to the new customer info page
        CustomerInforation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Customer Information']")))

        if CustomerInforation_text.is_displayed():
            print(CustomerInforation_text.text)
        else:
            print('Error occured at Navigate to the "New Customer Info" page')
        time.sleep(2) 
    except Exception as e:
        print('The error occured at Navigate to "New Customer Info page. Error: ', e)

# Enter all details
@then(u'Enter All details and Click on save button') 
def Enter_All_Details(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        Email_Input = context.driver.find_element(By.XPATH, Locators.Customeremail_input_xpath)
        Email_Input.send_keys(Email)
        print(f'Email ID: {Email}')
        time.sleep(1)

        Phone_Input = context.driver.find_element(By.XPATH, Locators.Customerphone_input_xpath)
        Phone_Input.send_keys(Mobile_no)
        print(f'Phone Number: {Mobile_no}')
        time.sleep(1)
        # Select a level from the list
        SelectLevel_Button = context.driver.find_element(By.XPATH, Locators.Selectlevel_dropdown_xpath)
        SelectLevel_Button.click()
        time.sleep(1)

        All_Levels_Options = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.All_levels_xpath))) 
        real_levels = [i for i in All_Levels_Options if i.text != "Select Level"]
        if All_Levels_Options:
            choice = random.choice(All_Levels_Options)
            print(choice.text)
            choice.click()
        time.sleep(1)  

        # Click on Calendar and select the date
        AccountOpened_Button = context.driver.find_element(By.XPATH, Locators.Accountopened_datepicker_xpath) 
        AccountOpened_Button.click()
        time.sleep(1) 

        Date, Month, Year = "3", "October", "2025"

        while True:

            AllDates = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.allActiveDates)))   
            Next_Button = wait.until(EC.presence_of_element_located((By.XPATH, Locators.Cal_Next_Button_xpath))) 

            Month_text = wait.until(EC.presence_of_element_located((By.XPATH, Locators.Cal_Month_Text_xpath)))
            print('The Present Moth: ', Month_text.text)

            Year_Text = wait.until(EC.presence_of_element_located((By.XPATH, Locators.Cal_Year_Text_xpath)))
            print('The Present Year: ', Year_Text.text)

            if Month_text.text == Month and Year_Text.text == Year:
                time.sleep(1)
                AllDates = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.allActiveDates))) 

                for day in AllDates:
                    if day.text == Date:
                        print("the date found", day.text)
                        day.click()
                        break
                break                        
            else:
                Next_Button.click()
                time.sleep(1)

        # End of while loop

        # Remaining details
        Presonal_ID = context.driver.find_element(By.XPATH, Locators.Personalid_input_xpath)
        Presonal_ID.send_keys(Area_code)
        print(f'The Personal ID is: {Area_code}')
        time.sleep(1)

        Street_Address = context.driver.find_element(By.XPATH, Locators.StreetAddress_input_xpath)
        Street_Address.send_keys(LastName)
        print(f'The Street Address is: {LastName}')
        time.sleep(1)

        City = context.driver.find_element(By.XPATH, Locators.City_input_xpath) 
        City.send_keys("Hyderabad")
        print("City Name is: Hyderabad") 
        time.sleep(1)

        State = context.driver.find_element(By.XPATH, Locators.State_input_xpath) 
        State.send_keys('Telangana')
        print('State: Telangana')
        time.sleep(1)

        ZipCode = context.driver.find_element(By.XPATH, Locators.zipcode_xpath)
        ZipCode.send_keys(Zip_code)
        print('The Zip code: ', Zip_code)
        time.sleep(1)

        Save_Button = context.driver.find_element(By.XPATH, Locators.Save_Button_xpath)
        Save_Button.click()



                    
    except Exception as e:
        print('The error occured at enter customer details. Error: ',e)    


    time.sleep(15)
@then(u'Verify user in the all users list')
def VerifyUserData(context):
    pass
