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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    table_countries = driver.find_element_by_css_selector('table.dataTable')
    rows_countries = table_countries.find_elements_by_css_selector('tr.row')
    list_countries = []
    for row_country in rows_countries:
        list_countries.append(row_country.find_element_by_xpath('./td[3]/a').get_attribute('href'))
    for list_country in list_countries:
        driver.get(list_country)
        table_zones = driver.find_element_by_css_selector('table#table-zones')
        rows_zones = table_zones.find_elements_by_css_selector('tr')
        rows_zones.pop(0)
        rows_zones.pop()
        get_items_and_assert(rows_zones, By.XPATH, './td[3]/select/option[@selected="selected"]')


def get_items_and_assert(items, *args):
    list_items = []
    for item in items:
        list_items.append(item.find_element(*args).text)
    sort_list_items = sorted(list_items)
    assert (list_items, sort_list_items)
