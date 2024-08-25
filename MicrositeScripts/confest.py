import bcolors
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        print(bcolors.OKBLUE + "Launching Chrome browser..." + bcolors.ENDC)
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'firefox':
        print(bcolors.OKBLUE + "Launching Firefox browser..." + bcolors.ENDC)
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        driver = webdriver.Firefox()
        print(bcolors.OKBLUE + "user not defined any specific browser :: Launching Firefox by default" + bcolors.ENDC)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# To Run tests
# pytest --html=report.html MicrositeScripts/MicroLoginscripts.py

# To Run tests on specific browser
# Terminal > pytest -s -v testCases/test_login.py --browser chrome
# Terminal > pytest -s -v testCases/test_login.py --browser firefox

# To Run tests parallel
# pytest -s -v -n=2 testCases/test_login.py --browser chrome
# pytest -s -v -n=2 testCases/test_login.py --browser firefox

################### PyTest HTML Report #########################
# It is hook for Adding Environment info to HTML Report


def pytest_configure(config):
    config.metadata = {
        "Tester": "Harshal",
        "Project Name": "Microsite LoginScripts",
        "Module Name ": "MicroLogin"
    }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
