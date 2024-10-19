class Locators_List:
    URL = "https://staging.servcrust.com/"
    Partner_Username = "Hanuman"
    Password = "Test@1234"
    Password1 = "Test@12345"

    # Login button
    LoginButton_Xpath = "//div[@id='navbarCollapse']//a[normalize-space()='Login']"

    # SignIn page
    WelcomeMessage_Xpath = "//h5[normalize-space()='Welcome to Order Management System.']"
    UserName_Xpath = "//input[@type='email']"
    Password_Xpath = "//input[@id='password']"
    SignIn_Button = "//button[@type='submit']"