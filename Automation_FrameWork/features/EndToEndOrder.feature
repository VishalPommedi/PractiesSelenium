Feature: As a customer, place an order from pega website
    Scenario Outline: Place a random order
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Select a product type from the list
        And Selet a product and click on "View Details Button"
        When I navigate to Details page
        Then Store the product price and click on order Button
        And verify order product page
        When Click on the Cart Button
        Then Click on the Next Button
        And Add Billing addres Details, select Shipping to Billing addres
        When Credit Card is selected on the "ell Us How You Will Pay" page
        Then Enter the card details
        And Click on the Submit Button
        And verify the Success message
        Then Logout
        And Close the Browser
    Examples:
    | UserName | Password |  
    | Vishal   | Test     |  