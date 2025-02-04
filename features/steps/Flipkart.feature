Feature: Flipkart Login

  Scenario: Successful login with valid credentials
    Given I open the Flipkart login page
    When I enter the valid username "testuser@example.com" and password "testpassword"
    And I click the login button
    Then I should be redirected to the homepage
    And I should see the user's name "Test User" on the homepage