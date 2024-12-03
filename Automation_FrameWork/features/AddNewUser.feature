Feature: Add a customer to the website
    Scenario Outline: Login with a user and add a random product to cart
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Navigate to customer page
        And Add Customer details "Account Number", "Customer Name", "Company Name", and click on "Add Customer button"
        When Navigated to the "New Customer page"
        Then Enter All details and Click on save button
        And Verify user in the all users list
        Then Logout
        And Close the Browser
    Examples:
    | UserName | Password |  
    | Vishal   | Test     |  