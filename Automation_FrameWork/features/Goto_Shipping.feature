Feature: Login as a user and Navigate the shipping page read the data and Logout
    Scenario Outline: Read the data from the shipping page
        Given I launch the Chrome Browser
        When I Navigated to the Pega Login page
        Then I Entered "<UserName>" and "<Password>"
        When User Login Successfully verify the user Name
        Then Select the shipping company, save the company title, and get back to the first window
        Then Logout
        And Close the Browser
    Examples:
        |UserName|Password|
        |Rajesh  |1234|      