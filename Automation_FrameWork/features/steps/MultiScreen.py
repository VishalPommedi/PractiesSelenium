from imports import *

Configurator = LogConfigurator()

@then(u'select the Shipping type from list')
def selectShipping(context):
    wait = WebDriverWait(context.driver, 10)
    Configurator.beforeall(context)
    Action = ActionChains(context.driver)

    try:
        menuList = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.allMenuOPtions_xpath)))

        menuOptions_names = [i.text for i in menuList]
        logging.info(f'The Menu list is: {menuOptions_names}')

        Shipping = next((i for i in menuList if i.text == "Shipping" ), None)

        if Shipping:
            logging.info(f'The {Shipping.text} found in the list')
            Action.move_to_element(Shipping).perform()
        else:
            logging.error(f'The {Shipping.text} is not found!')            

        ShippingSubMenu = wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators.shppingSubMenu_xpath)))

        shippingsubmenuNames = [i.text for i in ShippingSubMenu]

        logging.info(f'The Sub menu option is: {shippingsubmenuNames}')

        UPS = next((i for i in ShippingSubMenu if i.text == "UPS"), None)

        if UPS:
            logging.info(f'The {UPS.text} is found')
            UPS.click()
        else:
            logging.error(f'The {UPS.text} is not found!')

    except Exception as e:
        logging.error(f'The error is occured at the click on Shipping Sub Menu Option. The error is: {e}')
    time.sleep(10)        

@then(u'Read The data and close')
def ReadDatafromPage(context):

    try:


        Configurator.beforeall(context)

        context.CurrentWindow = context.driver.current_window_handle

        WebDriverWait(context.driver, 10).until(lambda d: len(context.driver.window_handles)>1)

        New_Window = [i for i in context.driver.window_handles if i != context.CurrentWindow][0]

        context.driver.switch_to.window(New_Window)

        time.sleep(5)

        NewPage = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-controls='subsection-shipping']")))

        if NewPage:
            logging.info('The page is loaded')
        else:
            logging.error('The page is not loaded')

        context.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)

        context.driver.execute_script('window.scrollTo(0, 0);')

        time.sleep(5)

        context.driver.close()
        logging.info('The New page is closed')
    except Exception as e:
        logging.error(f'The error is occred at switch to new page, and scroll. The error: {e}')
@then(u'Open first web page')
def SwitBack(context):
    context.driver.switch_to.window(context.CurrentWindow)
    logging.info('The driver is switch back to the first page')

    time.sleep(3)            