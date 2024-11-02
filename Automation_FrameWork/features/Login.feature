Feature: Register a user in demo webshop

  Scenario: Register a user in demo webshop
    Given I launch chrome broser
    When Navigate to the "<website>"
    Then I close the browser

    Example:
    |website|
    |https://staging.servcrust.com/"
