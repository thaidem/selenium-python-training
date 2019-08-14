import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_check_stickers(driver):
    driver.get("http://localhost/litecart/en/")
    stickers_list = driver.find_elements_by_css_selector('div.image-wrapper')
    for sticker in stickers_list:
        len_sticker = len(sticker.find_elements_by_css_selector('.sticker'))
        str_sticker = str(len_sticker)
        if len_sticker > 1:
            print("На карточке товара больше одного стикера: " + str_sticker)
        elif len_sticker == 0:
            print("На карточке товара ни одного стикера: " + str_sticker)
        else:
            print("На карточке товара один стикер: " + str_sticker)
