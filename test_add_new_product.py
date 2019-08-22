import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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


def test_check_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
#
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element(By.LINK_TEXT, 'Add New Product').click()

