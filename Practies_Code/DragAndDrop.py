import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DemoDragDrop():
    def DragDrop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://jqueryui.com/droppable/')

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        dragElement = driver.find_element(By.XPATH, "//div[@id='draggable']")
        dropElement  = driver.find_element(By.XPATH, "//div[@id='droppable']")
        # First Method
        ActionChains(driver).drag_and_drop(dragElement, dropElement).perform()

        # Second method
        # ActionChains(driver).drag_and_drop_by_offset(dragElement, 70, 120).perform()

        time.sleep(10)

Test = DemoDragDrop()

Test.DragDrop()