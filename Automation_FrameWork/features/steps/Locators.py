# Pega website web elements XPATHs

WebSite_URL = "https://training.openspan.com/login"

# Web page Menu

Menu_Options_xpath = "//div[@id='menu']//li/a"

# Stores
Stores_StoreListing_xpath = "//a[normalize-space()='Store Listing']"
StoerListing_Text_xpath = "//h1[normalize-space()='Store Listing']"
StoreListening_TableRows_xpath = "//table[@id='search_store_list']//tbody//tr"
StoreListening_TableCelss_xpath = "//table[@id='search_store_list']//tbody//tr//td"

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

NextButton_BillingPage_xpath = "//input[@value='Next' and @id='next2_button']"

# Gear Icon | Customers
Newcustomer_tabledata_xpath = "//table[@id='manage_user_inputs']//tbody//tr[2]//td"
Accountnumber_input_xpath = "//input[@id='account_number']"
Customername_input_xpath = "//input[@id='customer_name']"
Companyname_input_xpath = "//input[@id='company_name']"
Addcustomer_Button_xpath = "//input[@id='login_button']"

# Gear Icon | Customers | New Customer information
Customeremail_input_xpath = "//input[@id='account_email']"
Customerphone_input_xpath = "//input[@id='account_phone']"
Selectlevel_dropdown_xpath = "//select[@id='account_level']"
All_levels_xpath = "//select[@id='account_level']//option"
Accountopened_datepicker_xpath = "//input[@id='datepicker']"


# Calendar
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
allActiveDates = "//div[@id='ui-datepicker-div']//tbody/tr/td[@class!=' ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled']//a"
Cal_Month_Text_xpath = "//span[@class='ui-datepicker-month']"
Cal_Year_Text_xpath = "//span[@class='ui-datepicker-year']"
Cal_Next_Button_xpath = "//span[@class='ui-icon ui-icon-circle-triangle-e']"
Cal_Previous_Button_xpath = "//span[@class='ui-icon ui-icon-circle-triangle-w']"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Personalid_input_xpath = "//input[@id='account_ssn_code']"
StreetAddress_input_xpath = "//input[@id='account_street_address']"
City_input_xpath = "//input[@name='city']"
State_input_xpath = "//input[@id='account_state']"
zipcode_xpath = "//input[@id='account_zip_code']"
Save_Button_xpath = "//input[@name='Save']"
Cancel_Button_xpath = "//input[@name='Cancel']"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$-Finance page locators-$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
F_HomePage_xpath = "//b[normalize-space()='ACME Finance']"
F_GearIcon_xpath = "//div//ul//li//a[@class='menu_option']"
F_GearOptions_xpath = "//div[@class='submenu_option']//a"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$-Menu List locators-$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
allMenuOPtions_xpath = '//div[@id="menu"]//ul//li//a[@class="menu_option"]'
shppingSubMenu_xpath = "//div[@id='shipping_menu']//div//a"





