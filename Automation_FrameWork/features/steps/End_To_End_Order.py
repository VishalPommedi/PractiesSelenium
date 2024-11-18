import time
import Locators
import random
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

        time.sleep(2)



    except Exception as e:
        print('The error occured at to enter billing details')
        print(e)

    try:
        #Click on the Next Button
        NextButton = context.driver.find_element(By.XPATH, Locators.NextButton_BillingPage_xpath)
        print('The next buttton is: ', NextButton.is_enabled())
        NextButton.click()
        print('cliked on the "Next Button"')

    except Exception as e:
        print('The error uccred at clik on the "Next" Button on Billing Screen\n error: ', e)

    time.sleep(2)

@when(u'Credit Card is selected on the "ell Us How You Will Pay" page')
def Creck_CreditCard_Selected(context):

    try:    
        CreditCard = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.CreditCard_RadioButton_path))
        )

        if CreditCard.is_selected():
            print('The "Credit Card Selected By Default"')
        else:
            print('The Card is not selected')

    except Exception as e:
        print('The error occured at verify the "Credit Card" Radio button is selected by default')
        print('error: ', e)
    time.sleep(1)    

@then(u'Enter the card details')
def Enter_Card_Details(context):
    # Select the Card type
    try:
        CardType_Button = context.driver.find_element(By.XPATH, Locators.CardType_xpath)
        CardType_Button.click()
        time.sleep(1)

        AllCard_Types = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.CardTypeDropdown_xpath))
        )
        AllCards_Names = [i.text for i in AllCard_Types]
        FilterCards = [card_type for card_type in AllCard_Types if card_type.text != "Card Type"]
        print('Card Types: ', AllCards_Names)

        if FilterCards:
            card = random.choice(FilterCards)
            print(f'Selected Card: {card.text}')
            card.click()
    except Exception as e:
        print('the error occured at select the card type from the drop down')
        print(e)        
    time.sleep(1)
    # Enter Security code and Card Number
    try:
        SecurityCode = context.driver.find_element(By.XPATH, Locators.SecurityCode_xapth)
        SecurityCode.send_keys(Area_code)
        print("Entered the Security code: ",Area_code)
        time.sleep(1)

        CreditCard_Number = context.driver.find_element(By.XPATH, Locators.CardNumber_xpath)
        CreditCard_Number.send_keys(CC_Num)
        print(f'Credit card number: {CC_Num}')
        time.sleep(1)

    except Exception as e:
        print('the error occured at enter security code and credit card number\n', e)

    # Select the expiration month and year
    try:    
        ExpirationMonth_Button = context.driver.find_element(By.XPATH, Locators.ExpirationMonth_xpath)  
        ExpirationMonth_Button.click()
        print('Clicked on the Expiration month button')
        time.sleep(1)
        AllMonths = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.ExpirationMonthDropdown_xpath))
        )
        FilterMonths = [i for i in AllMonths if i.text != "Expiration Month"]
        AllMonths_Names = [i.text for i in AllMonths]
        print(f'All Months: {AllMonths_Names}')

        if FilterMonths:
            Month = random.choice(FilterMonths)
            Month.click()
            print(f'selected month: {Month.text}')
    except Exception as e:
        print('The error occured at click on the Expiration month\nerror: ',e)
    time.sleep(1)
    # Select Expiration Year
    try:
        ExpriationYear_Button = context.driver.find_element(By.XPATH, Locators.ExpirationsYear_xpath)
        ExpriationYear_Button.click()
        print('clicked on the Expiration year button')
        time.sleep(1)
        AllYears = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.ExpirationYearDropdown_xpath))
        )    

        year_text = [i.text for i in AllYears]
        print(year_text)
        FilterYears = [i for i in AllYears if i.text != "Expiration Year"]   

        if FilterYears:
            Year = random.choice(FilterYears)   
            Year.click()
            print('Selected year: ',Year.text)       

    except Exception as e:
        print('The error occured at select the expiration month and date\nerror:', e)  

    time.sleep(2)

@then(u'Click on the Submit Button')
def ClickOn_Submit_Button(context):
    try:
        Submit_Button = context.driver.find_element(By.XPATH, Locators.SubmitButton_xpath)
        Submit_Button.click()
        time.sleep(2)
    except Exception as e:
        print('The error occured at click on the Submit Button, error: ', e)
        print('The Button : ',Submit_Button.is_enabled())

@then(u'verify the Success message')
def Verify_SucessMessage(context):
    try:
        Order_Id = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div//p//b"))
        )

        print('The Order Id: ', Order_Id.text)
        time.sleep(1)

        Success_message = context.driver.find_element(By.XPATH, "//div//p[2]")
        print('the success message: ', Success_message.text)

    except Exception as e:
        print('The error occured at read the success message/n error: ',e)    
    time.sleep(2)