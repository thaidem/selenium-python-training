import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    # wd.implicitly_wait(10)
    # wait = WebDriverWait(driver, 10)
    request.addfinalizer(wd.quit)
    return wd


def test_cart(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://litecart.stqa.ru/en/")
    # driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector('.product').click()
    quantity = driver.find_element_by_css_selector('span.quantity')
    print(quantity.text)
    driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    wait.until(EC.staleness_of(quantity))
    quantity = driver.find_element_by_css_selector('span.quantity')
    print(quantity.text)
    # driver.get("https://litecart.stqa.ru/en/")
    # driver.find_element_by_css_selector('.product').click()
    # driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    # quantity = driver.find_element_by_css_selector('span.quantity')
    # print(quantity.text)
    # driver.refresh()
    # wait.until(EC.staleness_of(quantity))
    # driver.get("https://litecart.stqa.ru/en/")
    # driver.find_element_by_css_selector('.product').click()
    # driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    # quantity = driver.find_element_by_css_selector('span.quantity')
    # print(quantity.text)
    # driver.refresh()
    # wait.until(EC.staleness_of(quantity))
    # pass
