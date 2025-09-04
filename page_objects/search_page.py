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
            self._wait.until(EC.presence_of_element_located(self._search_page.SEARCH_BOX))
        except Exception as e:
            raise Exception("Google Maps did not load the search box in time") from e

    def click_skip_button(self):
        try:
            self._wait.until(EC.element_to_be_clickable(self._search_page.SKIP_BUTTON)).click()
        except:
            # Skip button may not appear on all app launches; ignore if not present
            pass

    def enter_search_text(self, text):
        self.click_search_box()
        editable_search_box = self._wait.until(EC.presence_of_element_located(self._search_page.SEARCH_BOX_EDIT))
        editable_search_box.clear()
        editable_search_box.send_keys(text)
        self._driver.press_keycode(66)
    
    def click_search_box(self):
        search_box = self._wait.until(EC.element_to_be_clickable(self._search_page.SEARCH_BOX))
        search_box.click()

    def click_directions_button(self, city):
        directions_btn = self._wait.until(EC.presence_of_element_located(
            (self._search_page.directions_button(city))
        ))
        directions_btn.click()

    def click_start_point(self):
        start_box = self._wait.until(EC.presence_of_element_located(
            (self._search_page.START_POINT)
        ))
        start_box.click()

    def enter_start_point(self, city):
        start_box = self._wait.until(EC.presence_of_element_located(
            (self._search_page.START_POINT)
        ))
        start_box.clear()
        start_box.send_keys(city)
        self._driver.press_keycode(66)
    
    def assert_navigation_modes_displayed(self):
        modes = ["Driving mode", "Transit mode", "Walking mode", "Bicycling mode"]
        
        for mode in modes:
            element = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, f"//android.widget.LinearLayout[contains(@content-desc, '{mode}')]")
                )
            )
            assert element.is_displayed(), f"{mode} is not displayed"

    def assert_preview_button(self):
        assert self._search_page.PREVIEW_BUTTON.is_displayed()


class AndroidSearchPage:
    """
    Page object for Google Maps search page.
    """

    SEARCH_BOX = (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
    SEARCH_BOX_EDIT = (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    SKIP_BUTTON = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.apps.maps:id/compass_container']/android.widget.LinearLayout")
    START_POINT = (AppiumBy.ACCESSIBILITY_ID, "Choose start location")
    PREVIEW_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Preview']")

    def __init__(self, driver):
        self._driver = driver

    @property
    def search_box(self):
        return self._driver.find_element(*self.SEARCH_BOX)

    @property
    def skip_button(self):
        return self._driver.find_element(*self.SKIP_BUTTON)
    
    def directions_button(self, city):
        return AppiumBy.XPATH, f"//android.widget.Button[@content-desc='Directions to {city}']"
