Feature: Read data from the shipping platforms
    Scenario Outline: Read data with all type of shipping platforms
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then select the Shipping type from list
        And Read The data and close
        And Open first web page
        Then Logout
        And Close the Browser
    Examples:
        | UserName | Password |
        | Vishal   | Test     |
