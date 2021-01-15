Feature: login functionality automation

  @smoke @regression
  Scenario: Verify login success
    Given the app is launched
    When User navigate to login page
    Then Verify user on login page
    When User login with username "test@email.com" and password "abcabc"
    Then Verify loggedin user