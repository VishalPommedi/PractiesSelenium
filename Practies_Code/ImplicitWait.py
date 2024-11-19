import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class ImplicitWait():
    def ImplicitWaitDemo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('https://login.salesforce.com/?locale=in')

        driver.find_element(By.NAME, "username").send_keys('Vishal')
        time.sleep(10)

Test = ImplicitWait()
Test.ImplicitWaitDemo()
