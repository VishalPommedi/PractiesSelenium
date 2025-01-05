from imports import *
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()

chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get("https://wrong.host.badssl.com/")

# wait = WebDriverWait(driver, 10)

# Advanced_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="nav-wrapper"]//button[contains(text(), "Advanced")]')))

# time.sleep(1)

# Advanced_button.click()

# time.sleep(1)

# Proceed_Button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="details"]//a[contains(text(), "Proceed")]')))

# Proceed_Button.click()

print(driver.title)

time.sleep(10)
driver.quit

