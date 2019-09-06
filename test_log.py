import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_check_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
#
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    table_products = driver.find_element_by_css_selector('table.dataTable')
    rows_products = table_products.find_elements_by_xpath('//td/img/following-sibling::a')
    list_products = []
    for row_product in rows_products:
        list_products.append(row_product.get_attribute('href'))
    for i in list_products:
        driver.get(i)
        for entry in driver.get_log('browser'):
            print(entry)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")

