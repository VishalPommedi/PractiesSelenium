from selenium import webdriver

def before_all(context): 
    print('setting up the webdriver...')
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()  

def after_all(context):
    print('closing the browser..')
    context.driver.quit()
