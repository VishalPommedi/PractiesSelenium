import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

class VerifyButtonClickable:

    user_name_xpath = "//input[@name='user_name']"
    password_xpath = "//input[@id='user_pass']"
    SignInButton_xpath = "//input[@id='login_button']"
    SelectProductType_xpath = "//select[@id='productType']"
    SelectProductOptions_xpath = "//select[@id='productType']//option"
    SelectProduct_xpath = "//select[@id='productsList']"
    AllProducts_xpath = "//select[@id='productsList']//option"
    ViewDetailsButton_xpath = "//input[@id='viewButton']"

    # View Details page
    AggregateName_xpath = "//div[@class='content']//table[@id='title_and_home_link']//tbody//tr//td//h1"
    OrderButton_xpath = "//input[@name='Order']"
    Quantity_xpath = "//select[@name='product_quantity']"
    QuantityList_xpath = "//select[@name='product_quantity']//option"

    # Cart Xpath's
    CountOfOrders_xpath = "//div//ul//div[@id='number_orders']"
    CartImage_xpath = "//div//ul/li//a//img[@alt='Cart']"
    

    def checkthebutton(self):

        try:
             driver = webdriver.Chrome()
             driver.maximize_window()
             driver.get("https://training.openspan.com/login")
             print('Naviagted to the pega website')
             time.sleep(5)
        except Exception as e:
            print('error occured at navigate to the website\n The error ', e)

        try:
            SignIn_Button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.SignInButton_xpath)))

            booln = SignIn_Button.is_enabled()

            print(booln)

            # Enter user name and password
            user_name = driver.find_element(By.XPATH, self.user_name_xpath)
            user_name.send_keys('testing')
            time.sleep(1)

            password = driver.find_element(By.XPATH, self.password_xpath)
            password.send_keys('testing')
            time.sleep(2)
            booln1 = SignIn_Button.is_enabled()
            print(booln1)

            if booln1:
                SignIn_Button.click()
        except Exception as e:
            print('The error is ', e)

        
        try:
            HomeScreen = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='ACME Product Search System']")))

            if HomeScreen.text == "ACME Product Search System":
                print(f'Home Screen: {HomeScreen.text}')
                time.sleep(5)

                Select_Product_dropdown = driver.find_element(By.XPATH, self.SelectProductType_xpath)
                Select_Product_dropdown.click()
                time.sleep(1)

                ProductOptions = driver.find_elements(By.XPATH, self.SelectProductOptions_xpath)
                productNames = [i.text for i in ProductOptions]
                originalproductOptions = [i for i in ProductOptions if i.text!="Select Product Type"]

                print(f'product names: {productNames}')
                
                if originalproductOptions:
                    randomproduct = random.choice(originalproductOptions)
                    randomproduct.click()
                    print(f'selected product: {randomproduct.text}')
                    time.sleep(5)
                
                SelectProductButton = driver.find_element(By.XPATH, self.SelectProduct_xpath)  
                SelectProductButton.click()
                time.sleep(3)

                AllProductsList = driver.find_elements(By.XPATH, self.AllProducts_xpath)
                OriginalProductNames = [i for i in AllProductsList if i.text  != "Select Product"]
                AllProductNames = [i.text for i in AllProductsList]
                print(f'{productNames} list {AllProductNames}')
                time.sleep(4)
                if OriginalProductNames:
                    SelectAProduct = random.choice(OriginalProductNames)
                    SelectAProduct.click()
                    print(f'Product Name: {SelectAProduct.text}') 
                    time.sleep(5)  

                # Click on the Veiw Details Button if it is Clickable
                View_Button = driver.find_element(By.XPATH, self.ViewDetailsButton_xpath)
                ButtonStatus = View_Button.is_enabled()
                print(f'View Details Button Status: {ButtonStatus}')

                if ButtonStatus:
                    View_Button.click()
                    print('clicked on the View Details button')
                    time.sleep(3)
                else:
                    print('the button is still disabled!')

                # Select Quantity and click on the Order Button
                Quantity_Button = driver.find_element(By.XPATH, self.Quantity_xpath)
                Quantity_Button.click()
                time.sleep(1)

                Quantity_list = driver.find_elements(By.XPATH, self.QuantityList_xpath)
                Ql = [i for i in Quantity_list]

                if Ql:
                    Random_Quantity = random.choice(Ql)
                    print(f'Selected Quantity: {Random_Quantity.text}')    
                    time.sleep(5)

                Order_Button = driver.find_element(By.XPATH, self.OrderButton_xpath)
                driver.execute_script("arguments[0].scrollIntoView(true);", Order_Button)
                # arguments[0].scrollIntoView(true);
                time.sleep(1)
                Order_Button.click()
                time.sleep(10)    



                # attempts = 3
                # for attempt in range(attempts):
                #     try:
                #         AggregateName = driver.find_element(By.XPATH, self.AggregateName_xpath)
                #         print(f'View page Product Name: {AggregateName.text} Selected Product Name: {SelectAProduct.text}')
                #         break
                #     except StaleElementReferenceException:
                #         print('Trying to print the Aggregate Name:',attempt)
                #         time.sleep(5)



                     


                    



            else:
                print('error occured')
                

        except Exception as e:
            print(f'error occured at Home screen\n error: {e}')
                





       

       

obj = VerifyButtonClickable()
obj.checkthebutton()        
