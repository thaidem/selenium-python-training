import pytest
from selenium import webdriver
import re


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    #wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_check_duck(driver):
    driver.get("http://localhost/litecart/en/")
    product_front = driver.find_element_by_css_selector('div#box-campaigns li.product')
#
    name_front = get_item(product_front, 'div.name')
    regular_price_front = get_item(product_front, '.regular-price')
    color_regular_front = color_conv(product_front, '.regular-price')
    assert (color_regular_front[0], color_regular_front[1], color_regular_front[2])
    assert (get_tag(product_front, '.regular-price'), 's')
#
    campaign_price_front = get_item(product_front, '.campaign-price')
    color_campaign_front = color_conv(product_front, '.campaign-price')
    eqv_color_campaign(color_campaign_front)
    assert (get_tag(product_front, '.campaign-price'), 'strong')
    eqv_font_size(get_font_size(product_front, '.campaign-price'), get_font_size(product_front, '.regular-price'))
#
    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    product_inside = driver.find_element_by_css_selector('div#box-product')
#
    name_inside = get_item(product_inside, 'h1')
    regular_price_inside = get_item(product_inside, '.regular-price')
    color_regular_inside = color_conv(product_inside, '.regular-price')
    assert (color_regular_inside[0], color_regular_inside[1], color_regular_inside[2])
    assert (get_tag(product_inside, '.regular-price'), 's')
#
    campaign_price_inside = get_item(product_inside, '.campaign-price')
    color_campaign_inside = color_conv(product_inside, '.campaign-price')
    eqv_color_campaign(color_campaign_inside)
    assert (get_tag(product_inside, '.campaign-price'), 'strong')
    eqv_font_size(get_font_size(product_inside, '.campaign-price'), get_font_size(product_inside, '.regular-price'))
#
    assert (name_front, name_inside)
    assert (regular_price_front, regular_price_inside)
    assert (campaign_price_front, campaign_price_inside)


def eqv_color_campaign(color_campaign):
    assert color_campaign[0] != 0, (color_campaign[1] == 0, color_campaign[2] == 0)


def color_conv(product_price, arg):
    return re.findall(r'\b\d+\b', get_color(product_price, arg))


def eqv_font_size(font_size_campaign, font_size_regular):
    if font_size_campaign > font_size_regular:
        print("Всё ок! " + str(font_size_campaign) + " больше чем " + str(font_size_regular))
    else:
        print("Куда смотрит мАркетинг?")


def get_color(driver, arg):
    color = driver.find_element_by_css_selector(arg).value_of_css_property('color')
    print(color)
    return color


def get_tag(driver, arg):
    tag = driver.find_element_by_css_selector(arg).get_attribute('localName')
    print(tag)
    return tag


def get_item(driver, arg):
    item = driver.find_element_by_css_selector(arg).get_attribute('innerText')
    print(item)
    return item


def get_font_size(driver, arg):
    font_size = driver.find_element_by_css_selector(arg).value_of_css_property('font-size')
    font_size_float = float(font_size.rstrip('px'))
    print(font_size)
    return font_size_float
