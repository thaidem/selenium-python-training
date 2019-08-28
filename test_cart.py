import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd


def test_cart(driver):
    wait = WebDriverWait(driver, 10)
#
    for s in range(3):
        driver.get("https://litecart.stqa.ru/en/")
        driver.find_element_by_css_selector('.product').click()
        if len(driver.find_elements_by_css_selector('[name="options[Size]"]')) != 0:
            Select(driver.find_element_by_css_selector('[name="options[Size]"]')).select_by_value('Large')
        quantity = driver.find_element_by_css_selector('span.quantity')
        new_quantity = int(quantity.text) + 1
        driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(new_quantity)))
    driver.find_element_by_css_selector('#cart .link').click()
#
    driver.find_element_by_css_selector('.act').click()
    while len(driver.find_elements_by_css_selector('[value="Remove"]')) != 0:
        driver.find_element_by_css_selector('[value="Remove"]').click()
        item = driver.find_element_by_css_selector('.dataTable td.item')
        wait.until(EC.staleness_of(item))
