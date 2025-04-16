Feature: Add a Random product to cart
    Scenario Outline: Login with a user and add a random product to cart
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Select a product type from the list
        And Selet a product and click on "View Details Button"
        When I navigate to Details page
        Then Store the product price and click on order Button
        And verify order product page
        Then Logout
        And Close the Browser
    Examples:
    | UserName | Password |  
    | Vishal   | Test     |  