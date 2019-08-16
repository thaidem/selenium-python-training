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
    product_list = driver.find_elements_by_css_selector('.product')
    for sticker in product_list:
        len_sticker = len(sticker.find_elements_by_css_selector('.sticker'))
        str_sticker = str(len_sticker)
        product_name = sticker.find_element_by_css_selector('.name').text
        if len_sticker > 1:
            print("На карточке товара " + product_name + " больше одного стикера: " + str_sticker)
        elif len_sticker == 0:
            print("На карточке товара " + product_name + " ни одного стикера: " + str_sticker)
        else:
            print("На карточке товара " + product_name + " один стикер: " + str_sticker)
