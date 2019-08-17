import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    #wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    #wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    #wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_check_duck(driver):
    driver.get("http://localhost/litecart/en/")
    product_front = driver.find_element_by_css_selector('div#box-campaigns li.product')
    name_front = get_name(product_front, '.name')
    color_regular_front = get_color(product_front, '.regular-price')
    color_campaign_front = get_color(product_front, '.campaign-price')
    font_size_regular_front = get_font_size(product_front, '.regular-price')
    font_size_campaign_front = get_font_size(product_front, '.campaign-price')
    eqv_font_size(font_size_campaign_front, font_size_regular_front)
    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")
    product_inside = driver.find_element_by_css_selector('div#box-product')
    name_inside = get_name(product_inside, 'h1')
    color_regular_inside = get_color(product_inside, '.regular-price')
    color_campaign_inside = get_color(product_inside, '.campaign-price')
    font_size_regular_inside = get_font_size(product_inside, '.regular-price')
    font_size_campaign_inside = get_font_size(product_inside, '.campaign-price')
    eqv_font_size(font_size_campaign_inside, font_size_regular_inside)
    assert (name_front, name_inside)
    assert (color_regular_front, color_regular_inside)
    assert (color_campaign_front, color_campaign_inside)


def eqv_font_size(font_size_campaign, font_size_regular):
    if font_size_campaign > font_size_regular:
        print("Всё ок! " + str(font_size_campaign) + " больше чем " + str(font_size_regular))
    else:
        print("Куда смотрит мАркетинг?")


def get_color(driver, arg):
    color = driver.find_element_by_css_selector(arg).value_of_css_property('color')
    print(color)
    return color


def get_name(driver, arg):
    name = driver.find_element_by_css_selector(arg).text
    print(name)
    return name


def get_font_size(driver, arg):
    font_size = driver.find_element_by_css_selector(arg).value_of_css_property('font-size')
    print(float(font_size.rstrip('px')))
    return font_size
