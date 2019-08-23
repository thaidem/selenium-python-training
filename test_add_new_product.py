import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime


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


def test_add_new_product(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
#
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element(By.LINK_TEXT, 'Add New Product').click()
    driver.find_element_by_css_selector('input[type="radio"][value="1"]').click()
    driver.find_element_by_css_selector('[name="name[en]"]').send_keys("Big Duck")
    driver.find_element_by_css_selector('[name="code"]').send_keys("1111111")
    driver.find_element_by_css_selector('input[name="categories[]"][value="0"]').click()
    driver.find_element_by_css_selector('input[name="categories[]"][value="1"]').click()
    driver.find_element_by_css_selector('input[name="product_groups[]"][value="1-3"]').click()
    driver.find_element_by_css_selector('input[name="quantity"]').clear()
    driver.find_element_by_css_selector('input[name="quantity"]').send_keys("11")
    select = Select(driver.find_element_by_css_selector('select[name="sold_out_status_id"]'))
    select.select_by_visible_text('-- Select --')
    driver.find_element_by_css_selector('input[name="new_images[]"]').send_keys(os.getcwd() + "/bigduck.jpg")
    driver.find_element_by_css_selector('input[name="date_valid_from"]')\
        .send_keys(Keys.HOME + datetime.today().strftime("%d%m%Y"))
#
    driver.find_element(By.LINK_TEXT, 'Information').click()
    select = Select(driver.find_element_by_css_selector('select[name="manufacturer_id"]'))
    select.select_by_value("1")
    driver.find_element_by_css_selector('input[name="keywords"]').send_keys("big duck")
    driver.find_element_by_css_selector('input[name="short_description[en]"]').send_keys("It's very big duck")
    driver.find_element_by_css_selector('div.trumbowyg-editor')\
        .send_keys("This unbelievable big duck should like your!")
    driver.find_element_by_css_selector('input[name="head_title[en]"]').send_keys("Very big duck for sale")
    driver.find_element_by_css_selector('input[name="meta_description[en]"]').send_keys("This big duck for your")
#
    driver.find_element(By.LINK_TEXT, 'Prices').click()
    driver.find_element_by_css_selector('input[name="purchase_price"]').clear()
    driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys("1000")
    select = Select(driver.find_element_by_css_selector('select[name="purchase_price_currency_code"]'))
    select.select_by_value("USD")
    driver.find_element_by_css_selector('input[name="gross_prices[USD]"]').clear()
    driver.find_element_by_css_selector('input[name="gross_prices[USD]').send_keys("1200")
    driver.find_element_by_css_selector('input[name="gross_prices[EUR]"]').clear()
    driver.find_element_by_css_selector('input[name="gross_prices[EUR]').send_keys("1000")
    driver.find_element_by_css_selector('button[name="save"]').click()
#
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    table_product = driver.find_element_by_css_selector('table.dataTable')
    rows_product = table_product.find_elements_by_css_selector('tr.row')
    for item in rows_product:
        if item.find_element(By.XPATH, './td[3]').text == "Big Duck":
            print("Новый товар найден в каталоге!")
