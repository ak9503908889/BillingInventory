import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ebilling.rudramtech.in/index.php")
    request.cls.driver = driver
    yield
    driver.quit()