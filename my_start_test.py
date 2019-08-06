import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_check_url(driver):
    driver.get("http://software-testing.ru/edu/catalogue")
    driver.find_element_by_link_text('Selenium WebDriver: полное руководство').click()
    driver.find_element_by_class_name('btn-sign').click()
