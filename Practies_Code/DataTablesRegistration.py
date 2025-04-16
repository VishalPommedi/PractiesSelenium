import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Registration:

    def __init__(self, url):
        self.url = url
    def registerUser(self):
        try:
            
            # chrome_optoin = Options()
            # chrome_optoin.add_argument("--headless")

            driver = webdriver.Chrome()
            print('Open Browser')
            driver.maximize_window()
            print(f'Navigate to {self.url}')
            driver.get(self.url)

            Register = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Login / Register')]")))
            print('click on the Register Button')
            Register.click()
            time.sleep(2)

        except Exception as e:
            print(f'The error occured at click on the Login page. The error: {e}')

        try:
           wait = WebDriverWait(driver, 10)

           RegistrationPageMessage = wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Already registered? Sign-in:']"))) 

           assert RegistrationPageMessage == "Already registered? Sign-in:", "The Registation page is OPened"

        except Exception as e:
            print(f'The Error occured at Register a new user. The error is: {e}')


        try:
            
            

            close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@title='Close'])[2]")))
            close_button.click()
            print('clicked on the close button')

        except Exception as e:
            print(f'The error is occured at click on the close button. the error {e}')


url = "https://datatables.net"
obj = Registration(url)
obj.registerUser()
