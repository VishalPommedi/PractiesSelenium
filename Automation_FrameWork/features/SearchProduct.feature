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
    | Zip_Number |
    |  123456     |
    @test
    Scenario: login as a customer, and search the nearest stores with city name and state
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Click on the stores Button
        And Enter the city name and select the state from the dropd-dwon
        And read the store address
        When Nivaigate to the Home page
        Then Logout
        And Close the Browser
    