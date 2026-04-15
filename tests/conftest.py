import pytest
from selenium import webdriver

# Używane kiedy chcemy, aby wszystkie testy przeszły przez kąkretną przeglądarkę, wybrana w konfiguracji
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver...")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise Exception(f"Invalid browser. Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver.")
    my_driver.quit()

# Używane kiedy chcemy, aby wszystkie testy przeszły przez różne przeglądarki

# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     browser = request.param
#     print(f"Creating {browser} driver...")
#     if browser == "chrome":
#         my_driver = webdriver.Chrome()
#     elif browser == "firefox":
#         my_driver = webdriver.Firefox()
#     else:
#         raise Exception(f"Invalid browser. Expected 'chrome' or 'firefox', but got {browser}")
#     yield my_driver
#     print(f"Closing {browser} driver.")
#     my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome, firefox)"
    )