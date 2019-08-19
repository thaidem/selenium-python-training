import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Ie()
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_check_stickers(driver):
    driver.get("http://localhost/litecart/en/")
    name_front = driver.find_element_by_css_selector('#box-campaigns li.product div.name').get_attribute('innerText')
    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    name_inside = driver.find_element_by_css_selector('#box-product h1.title').get_attribute('innerText')
    assert (name_front, name_inside)
