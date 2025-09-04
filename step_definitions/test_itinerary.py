import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers


@scenario("../features/itinerary.feature", "When I launch the app, I can start an itinerary")
def test_itinerary():
    """BDD scenario for starting an itinerary in Google Maps."""
    pass


@given("the Google Maps App is opened")
def google_maps_opened(search_page):
    """
    Ensure Google Maps home page is loaded.
    Dismiss skip button if present.
    """
    try:
        search_page.load_maps_page()
    except:
        search_page.click_skip_button()


@when(parsers.parse("I search for '{city}'"))
def search_for_city(search_page, city):
    """Search for a given city in Google Maps."""
    search_page.enter_search_text(city)


@when(parsers.parse("I start an itinerary towards '{city}'"))
def start_itinerary(search_page, city):
    """Start itinerary to a city."""
    search_page.click_directions_button(city)


@when(parsers.parse("I change the starting point to '{city}'"))
def change_starting_point(search_page, city):
    """Change starting point of itinerary."""
    search_page.click_start_point()
    search_page.enter_search_text(city)


@then("the itinerary should show directions between starting point and destination")
def assert_itinerary_directions_shown(search_page):
    """Verify itinerary directions."""
    search_page.assert_navigation_modes_displayed()
    search_page.assert_preview_button()

