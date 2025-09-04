import pytest
from appium import webdriver
from time import sleep
from appium.webdriver.appium_service import AppiumService
from test_base.config import PlatformSettings
from appium.options.android import UiAutomator2Options


def android_desired_caps():
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": PlatformSettings.get_platform_version(),
            "appActivity": "com.google.android.maps.MapsActivity",
            "uiautomator2ServerInstallTimeout": 90000,
            "appPackage": "com.google.android.apps.maps",
            "appActivity": "com.google.android.maps.MapsActivity",
            "deviceName": "Pixel 4a",
            "udid": "emulator-5554",
            "noReset": True # Prevents re-install every run
        }
    )
    return options


def get_driver():
    url_base = "http://localhost:4723"
    return webdriver.Remote(url_base, options=android_desired_caps())
