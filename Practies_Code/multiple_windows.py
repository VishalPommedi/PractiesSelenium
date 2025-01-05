from imports import *
import time

class multiple_windows:
    def __init__(self, url):
        self.url = url
    def OpenBrowser(self):

        try:

            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(self.url)

        except Exception as e:
            print(f'The error occured at open the chrome browser. The error is: {e}')
        time.sleep(10)
    def CloseBrowser(self):
        self.driver.quit()

url = "https://demoqa.com/browser-windows"
obj = multiple_windows(url)

obj.OpenBrowser()
obj.CloseBrowser()

        
