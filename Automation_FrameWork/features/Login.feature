Feature: login to Pega website with a valid user
  Scenario Outline: Login with given credentials
    Given I launch the Chrome Browser
    When I Navigated to the Pega Login page
    Then I Entered "<UserName>" and "<Password>"
    When User Login Successfully verify the user Name
    Then Logout
    And Close the Browser

  Examples:
    | UserName | Password |
    | Testing  | Testing  |

