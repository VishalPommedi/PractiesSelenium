# Pega website web elements XPATHs

WebSite_URL = "https://training.openspan.com/login"

# login page
user_name_xpath = "//input[@name='user_name']"
password_xpath = "//input[@id='user_pass']"
SignInButton_xpath = "//input[@id='login_button']"
LoginPage_Message_xpath = "//h1[normalize-space()='Sign in to Pega Robotic Automation Training']"

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

ProductPrice_xpath = '//table[@id="home_product_detail"]//tbody//tr//td[2]//p[3]//b'

# Cart Xpath's
CountOfOrders_xpath = "//div//ul//div[@id='number_orders']"
CartImage_xpath = "//li[@id='cart_menu']//a[@class='menu_option']"

# Order Page
ContinueShopping_button_xpath = '//input[@name="continue_shopping"]'
EditYourCart_xpath = "//input[@name='edit_your_cart']"
ViewButton_xpath = "//a[contains(text(),'View')]"
RemoveButton_xpath = "//a[contains(text(),'Remove')]"
NextButton_xpath = '//input[@id="next1_button"]' # for all pages
GrandTotalValue_xpath = "//p[@id='your_total']//span"

# Step 2 Tell Us Who You Are
FirstName_xpath = "//input[@id='bfirst_name']"
LastName_xapth = "//input[@id='blast_name']"
CompanyName_xapth = "//input[@id='bcompany_name']"
StreetAddress_xpath = "//p//input[@name='bstreet_address']"
ZipCode_xapth = "//p//input[@name='bzip_code']"
AreaCode_xapth = "//p//input[@id='barea_code']"
PrimaryPhoneNumber_xapth = "//p//input[@name='bprimary_phone']"
ShipToBillingAddress_xpath = "//a[normalize-space()='Ship to Billing Address']"

# Step 3 Tell Us How You Will Pay
CreditCard_RadioButton_path = "//input[@id='credit_card']"
BillMe_xapth = "//input[@id='bill_me']"
CardType_xpath = "//select[@id='card_type']"
CardTypeDropdown_xpath = '//select[@name="card_type"]//option'
SecurityCode_xapth = "//input[@id='security_code']"
CardNumber_xpath = "//input[@id='card_number']"
ExpirationMonth_xpath = "//select[@id='expiry_month']"
ExpirationMonthDropdown_xpath = "//select[@id='expiry_month']//option"
ExpirationsYear_xpath = "//select[@id='expiry_year']"
ExpirationYearDropdown_xpath = "//select[@id='expiry_year']//option"
SubmitButton_xpath = "//input[@id='submit_button']"



