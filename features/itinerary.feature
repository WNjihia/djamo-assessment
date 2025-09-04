Feature: Itinerary planning in Google Maps
  As a user
  I want to start an itinerary
  So that I can get directions between cities

  Scenario: When I launch the app, I can start an itinerary
    Given the Google Maps App is opened
    When I search for 'Abidjan'
    And I start an itinerary towards 'Abidjan'
    And I change the starting point to 'Dakar'
    Then the itinerary should show directions between starting point and destination