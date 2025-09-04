import pytest
from test_base.driver_setup import get_driver
from page_objects.search_page import SearchPageActions


@pytest.fixture(scope="session")
def driver():
    """
    Initialize and quit the Appium driver.
    Session scope: reuse one driver instance across all tests.
    """
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    """
    Provide a SearchPage instance with the active driver.
    """
    return SearchPageActions(driver)


@pytest.mark.tryfirst
def pytest_bdd_after_scenario(request, feature, scenario):
    """
    Hook that runs after each BDD scenario.
    Useful for logging, screenshots, or cleanup.
    """
    print(f"After scenario: {scenario.name}")

