import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers

# scenario = partial(scenario, "../features/itinerary.feature")


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
    search_page.load_maps_page()
    search_page.click_skip_button()


@when(parsers.parse("I search for '{city}'"))
def search_for_city(search_page, city):
    """Search for a given city in Google Maps."""
    search_page.enter_search_text(city)


@then(parsers.parse("I should see search results for '{city}'"))
def verify_search_results(search_page_actions, city):
    """
    Assert that search results are displayed.
    """
    search_box = search_page_actions._driver.find_element_by_id(
        "com.google.android.apps.maps:id/search_omnibox_text_box"
    )
    assert city.lower() in search_box.text.lower(), f"Expected {city} in search box"
