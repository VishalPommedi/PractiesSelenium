from selenium.webdriver.common.by import By
from behave import *

@given(u'I launch chrome broser')
def Launch_Browser(context):
    context.driver.get("https://staging.servcrust.com/")
    