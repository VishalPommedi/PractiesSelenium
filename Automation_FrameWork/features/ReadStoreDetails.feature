Feature: As a user login to openspan.com and read the store data
    Scenario Outline: Login to openspan.com website and read the store data
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Navigate to "Store Listing" page
        And read the data
        Then Logout
        And Close the Browser
    Examples:
    |UserName|Password |
    | Vicky  | Test@123|