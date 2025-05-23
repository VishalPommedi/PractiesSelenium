@pega
Feature: Login as a user and search for the nearest stores with city name and pin code.
    Scenario Outline: Search nearest store using the pin code.
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Click on the stores Button
        And Enter the "<Zip_Number>" then click on "FInd Store" Button
        And read the store address
        Then Logout
        And Close the Browser
    Examples:
    | UserName | Password |  Zip_Number |
    | Vishal   | Test     |  123456     |