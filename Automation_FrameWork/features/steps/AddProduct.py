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
        print(f'The selected product is: "{SelectAProduct.text}"')

        time.sleep(4)

        # Verify the button is eneble before going to click on "View Details"
        View_Details_Button = context.driver.find_elemet(By.XPATH, Locators.ViewDetailsButton_xpath)

        View_Details_Button.click()    

        time.sleep(15)    

    except Exception as e:
        print(f'The error occured to select a product and click on the view details button')


        

@when(u'I navigate to Details page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I navigate to Details page')


@then(u'Store the product price and click on order Button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Store the product price and click on order Button')


@then(u'verify order product page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify order product page')