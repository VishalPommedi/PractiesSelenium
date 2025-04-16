Feature: As a admin login to the orange hrm website, read the profile data
    Scenario: login as an admin and read the profile data
        Given Launch the broser
        When Open the Orange HRM webapp
        Then Login with user name, and password
        And Naviate to the profile options and click on the About button
        And Read the user data
        Then Logout from page
        And close the web browser
