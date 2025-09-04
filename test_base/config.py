class PlatformSettings:
    _PLATFORM = ""
    _APP_LOCATION = ""
    _DEVICE_UDID = ""
    _PLATFORM_VERSION = ""
    _APP_PACKAGE = ""

    @classmethod
    def get_platform(cls):
        if PlatformSettings._PLATFORM is None:
            PlatformSettings._PLATFORM = "android"

        return PlatformSettings._PLATFORM
    
    @classmethod
    def set_platform(cls, platform: str):
        PlatformSettings._PLATFORM = platform.lower()

    @classmethod
    def set_platform_version(cls, version_number: str):
        if version_number is None:
            if PlatformSettings._PLATFORM == "android":
                PlatformSettings._PLATFORM_VERSION = "16.0"
        else:
            PlatformSettings._PLATFORM_VERSION = version_number

    @classmethod
    def get_platform_version(cls):
        return PlatformSettings._PLATFORM_VERSION
    
    @classmethod
    def set_package(cls):
        if PlatformSettings._PLATFORM == "android":
            PlatformSettings._APP_PACKAGE = "com.google.android.apps.maps"

    @classmethod
    def get_app_package(cls):
        return PlatformSettings._APP_PACKAGE