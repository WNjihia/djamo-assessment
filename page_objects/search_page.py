from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


class SearchPage:
    """
    Returns platform-specific page objects.
    """

    def __init__(self, driver):
        self._driver = driver

    @property
    def get_search_page(self):
        return AndroidSearchPage(self._driver)


class SearchPageActions:
    """
    Encapsulates actions a user can perform on the search page.
    """

    def __init__(self, driver):
        self._driver = driver
        self._search_page = SearchPage(driver).get_search_page
        self._wait = WebDriverWait(driver, 30)

    def load_maps_page(self):
        """
        Waits for the Google Maps search box to appear.
        This is a stable indicator that the app is ready for interaction.
        """
        try:
            print(self._driver.page_source)
            self._wait.until(EC.presence_of_element_located(AndroidSearchPage.SEARCH_BOX))
        except Exception as e:
            raise Exception("Google Maps did not load the search box in time") from e

    def click_skip_button(self):
        try:
            self._wait.until(EC.element_to_be_clickable(AndroidSearchPage.SKIP_BUTTON)).click()
        except:
            # Skip button may not appear on all app launches; ignore if not present
            pass

    def enter_search_text(self, text):
        search_box = self._wait.until(EC.element_to_be_clickable(AndroidSearchPage.SEARCH_BOX))
        search_box.click()
        search_box.send_keys(text)


class AndroidSearchPage:
    """
    Page object for Google Maps search page.
    """

    SEARCH_BOX = (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
    SKIP_BUTTON = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.apps.maps:id/compass_container']/android.widget.LinearLayout")

    def __init__(self, driver):
        self._driver = driver

    @property
    def search_box(self):
        return self._driver.find_element(*self.SEARCH_BOX)

    @property
    def skip_button(self):
        return self._driver.find_element(*self.SKIP_BUTTON)
