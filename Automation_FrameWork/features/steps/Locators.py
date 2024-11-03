# Pega website web elements XPATHs

WebSite_URL = "https://training.openspan.com/login"

# login page
user_name_xpath = "//input[@name='user_name']"
password_xpath = "//input[@id='user_pass']"
SignInButton_xpath = "//input[@id='login_button']"

# Home Screen

SelectProductType_xpath = "//select[@id='productType']"
SelectProductOptions_xpath = "//select[@id='productType']//option"
SelectProduct_xpath = "//select[@id='productsList']"
AllProducts_xpath = "//select[@id='productsList']//option"
ViewDetailsButton_xpath = "//input[@id='viewButton']"
HomeScreen_Text_xpath = "//h1[normalize-space()='ACME Product Search System']"
ExpectedHomeScreen_text = "ACME Product Search System"
GearIcon_xpath = "//ul//li[@id='profile_menu']//a[@class='menu_option']"
Profile_Details_xpath = "//div[@id='profile']//div//a"

# View Details page
AggregateName_xpath = "//div[@class='content']//table[@id='title_and_home_link']//tbody//tr//td//h1"
OrderButton_xpath = "//input[@name='Order']"
Quantity_xpath = "//select[@name='product_quantity']"
QuantityList_xpath = "//select[@name='product_quantity']//option"

# Cart Xpath's
CountOfOrders_xpath = "//div//ul//div[@id='number_orders']"
CartImage_xpath = "//div//ul/li//a//img[@alt='Cart']"


