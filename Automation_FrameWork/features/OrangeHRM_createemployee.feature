Feature: As a admin login to the orange hrm website, read the profile data
    Scenario: login as an admin and read the profile data
        Given Launch the broser
        When Open the Orange HRM webapp
        Then Login with user name, and password
        When Navigate to the PIM page
        Then goto the add employee tab
        And create a new employee with login details
        And verify the employee is created successfully
        Then Logout from page
        And close the web browser
    # Scenario: login as an admin and read the profile data
    #     Given Launch the broser
    #     When Open the Orange HRM webapp
    #     Then Login with the new employee user name, and password
    #     And verify the employee is created successfully
    #     Then Logout from page
    #     And close the web browser