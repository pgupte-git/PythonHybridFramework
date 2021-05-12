import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from TestData.ReadLoginData import ReadLoginData


def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="chrome")
    parser.addoption("--url", action="store")


@pytest.fixture()
def setup(browser, url, request):
    # browsername = request.config.getoption("--browsername") # It will return the browsername
    # url = request.config.getoption("--url") # It will return the
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("No browser is selected in run time, so by default it is running on chrome")

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)

    request.cls.driver = driver  # It is used to call this driver in to the test cases as local driver

    yield

    driver.close()


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browsername")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")
