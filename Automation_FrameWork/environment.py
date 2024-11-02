from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def browser(context):
    # Set up the WebDriver
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    yield context.driver
    # Tear down the WebDriver
    context.driver.quit()

def before_all(context):
    # Use the browser fixture
    use_fixture(browser, context)


