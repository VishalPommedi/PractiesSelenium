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

    # User role on Dashboard page

    UserButton_Xpath = "//button[@id='page-header-user-dropdown']"

    UserRole_Xpath = "//button[@type='button']//span//span[@class='d-none d-xl-block ms-1 fs-12 text-muted user-name-sub-text']"

    SignOutButton_Button = "//span[normalize-space()='Sign Out']"

    # User profile
    UserProfileButton_Xpath = "//a[@routerlink='/user-profile']"
    UserProfileDataRows_Xpath = "//div[@class='table-responsive']//table//tbody//tr"