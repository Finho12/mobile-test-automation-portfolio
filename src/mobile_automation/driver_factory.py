from appium import webdriver
from appium.options.android import UiAutomator2Options

from mobile_automation.config import settings


def create_driver():
    """Cria a sessão Appium usando configurações locais, sem hardcode do dispositivo."""
    if not settings.android_udid.strip():
        raise ValueError("Configure ANDROID_UDID no arquivo .env.")
    if not settings.app_package.strip():
        raise ValueError("Configure APP_PACKAGE no arquivo .env.")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = settings.android_device_name
    options.udid = settings.android_udid
    options.app_package = settings.app_package
    options.no_reset = settings.no_reset

    return webdriver.Remote(settings.appium_server_url, options=options)
