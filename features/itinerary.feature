Feature: Itinerary
    As a user 
    I want to search for a location and start an itinerary


    Scenario: When I launch the app, I can start an itinerary
        Given the Google Maps App is opened
        When I search for 'Abidjan'
        Then I should see search results for 'Abidjan'
