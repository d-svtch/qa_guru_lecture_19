import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

import config

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Google Pixel 7 Pro",

        # Set URL of the application under test
        "app": config.app,
        "appWaitActivity": "org.wikipedia.*",



        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": config.bstack_userName,
            "accessKey": config.bstack_accessKey
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
