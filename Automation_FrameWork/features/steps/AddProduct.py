import time
import random
import Locators
from behave import when, then 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then(u'Select a product type from the list')
def Select_A_ProductType(context):
    try:
        # Select a product type from the list
        ProductType_list_Button = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.SelectProductType_xpath)))
        ProductType_list_Button.click()
        time.sleep(1)
        ProductTypes_List = context.driver.find_elements(By.XPATH, Locators.SelectProductOptions_xpath)
        NamesOfAllProductTypes = [i for i in ProductTypes_List if i.text != "Select Product Type"]

        # For loop for selecting a random product
        SelectAProduct = random.choice(NamesOfAllProductTypes)
        print(f'Seleted Product type is "{SelectAProduct.text}"')
        SelectAProduct.click()
        time.sleep(2)
    except Exception as e:
        print('error occured at seleting a product type from the list\n the error', e)    



@then(u'Selet a product and click on "View Details Button"')
def SelectAProduct(context):
    try:
        # Select a random product from all product list except "Select Product"
        AllProduct_List_Button = context.driver.find_element(By.XPATH, Locators.SelectProduct_xpath)
        AllProduct_List_Button.click()
        print('clicked on the "Select product button')
        time.sleep(1)
        AllProducts_List = WebDriverWait(context.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.AllProducts_xpath)))
        NamesOfTheProduct = [i for i in AllProducts_List if i != "Select Product"]

        SelectAProduct = random.choice(NamesOfTheProduct)
        SelectAProduct.click()
        context.selectedproduct_name = SelectAProduct.text
        print(f'The selected product is: "{context.selectedproduct_name}"')
        
        time.sleep(2)

    except Exception as e:
        print(f'The error occured to select a product and click on the view details button/n The error: {e}')
        raise e

    
    try:
         # Verify the button is eneble before going to click on "View Details"
         ViewDetails_Button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.ViewDetailsButton_xpath)))
         print("The status of button", ViewDetails_Button.is_enabled())
         ViewDetails_Button.click()  
         time.sleep(2)  

    except Exception as e:
        print(f'The error occured to click on view details button')

@when(u'I navigate to Details page')
def OrderTheProduct(context):
    
    Aggregate_name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.AggregateName_xpath))
    )
    print('Expected name', context.selectedproduct_name)
    print('Output name ', Aggregate_name.text)

    if Aggregate_name.text == context.selectedproduct_name:
        print('The same name shown on view details page')
    else:
        print('the same name not shown on the view details page')

    time.sleep(2)    


@then(u'Store the product price and click on order Button')
def Click_On_OrderButton(context):
    # Store the bill amount
    try:
        ProductPrice = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.ProductPrice_xpath))
        )

        print(ProductPrice.text)
        time.sleep(3)
    except Exception as e:
        print('Error occured to save the product price')
        print('The error:', e)

    # Click on the order button
    try:
        Order_Button = context.driver.find_element(By.XPATH, Locators.OrderButton_xpath)
        Order_Button.click()
        time.sleep(15)
    except Exception as e:
        print('The erro occured to click on the "order button"')
        print('The error ', e)


@then(u'verify order product page')
def VerifyOrders_page(context):
    try:
        ContinueShopping_Button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.ContinueShopping_button_xpath))
        )

        if ContinueShopping_Button.is_displayed():
            print('The "Order Page" Visible')
        else:
            print('The "Order Page" is not Visible')

    except Exception as e:
        print('Error occured at navigate to Orders page')