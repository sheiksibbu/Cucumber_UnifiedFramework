@Smoke

Feature: Login to OrangeHRM and verify home page


  @Login @Smoke1234

  Scenario: Successful login and home page verification
    Given the user navigates to the OrangeHRM login page
    When the user enters valid credentails
    And clicks the Login button
    Then the user should be redirected to the home page
    And the page title should be OrangeHRM
    And the dashboard should display OrangeHRM Logo



  @Login @Smoke12345

  Scenario: Successful login and home page verification2
    Given the user navigates to the OrangeHRM login page
    When the user enters valid credentails
    And clicks the Login buttton
    Then the user should be redirected to the home page
    And the page title should be OrangeHRM
    And the dashboard should display OrangeHRM Logo

