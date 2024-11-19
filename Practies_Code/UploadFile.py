import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

current_path = os.path.dirname(os.path.abspath(__file__))


imagePath = os.path.join(current_path, "Images", "testimage.png")
print(imagePath)

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://plupload.com/examples/')
print('*Navigated to the Website')


AddFiles_Button = driver.find_element(By.ID, "uploader_browse")

driver.execute_script("arguments[0].scrollIntoView();", AddFiles_Button)

AddFiles_Button.click()
print('*Clicked on the AddFiles Button')

time.sleep(5)

keboard = Controller()
keboard.type(imagePath)
keboard.press(Key.enter)
keboard.release(Key.enter)

time.sleep(5)

driver.close()