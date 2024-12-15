Feature: As a Finance user login to finace page, and delete the changes
  Scenario Outline: login to finace page, and delete the changes
    Given I launch the Chrome Browser
    When I Navigated to the Pega Login page
    Then I Entered "<UserName>" and "<Password>"
    When User Login Successfully verify the user Name
    Then Select Finance under the Gear Icon
    And Enter the Finance User name and Password and login
    When Naviagated to the Finance Home page
    Then Select Del Chgs and Accept it
    And Close the tab
    Then Logout
    And Close the Browser

  Examples:
    | UserName | Password |
    | Vishal  | Testing  |

