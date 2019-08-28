import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd


def test_sign_login(driver):
    driver.get("https://litecart.stqa.ru/en/")
    # driver.get("http://localhost/litecart/en/")
    email = "dem11113@gmail.com"
    password = "260596"
    get_login(driver, email, password)
    if len(driver.find_elements(By.LINK_TEXT, 'Logout')) > 0:
        print("Такой email зарегистрирован, введите другой")
        driver.quit()
#
    driver.find_element_by_css_selector('table a').click()
    driver.find_element_by_css_selector('[name="firstname"]').send_keys("Dmitry")
    driver.find_element_by_css_selector('[name="lastname"]').send_keys("Kozlov")
    driver.find_element_by_css_selector('[name="address1"]').send_keys("5-24 49th Ave Apt.1 Long Island City")
    driver.find_element_by_css_selector('[name="postcode"]').send_keys("11101")
    driver.find_element_by_css_selector('[name="city"]').send_keys("New York")
    driver.find_element_by_css_selector('.select2-selection').click()
    driver.find_element_by_css_selector('input.select2-search__field')\
        .send_keys("United States" + Keys.ENTER)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('[value="NY"]').click()
    driver.find_element_by_css_selector('[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('[name="phone"]').send_keys(Keys.HOME + "+1-910-336-0370")
    driver.find_element_by_css_selector('[name="password"]').send_keys(password)
    driver.find_element_by_css_selector('[name="confirmed_password"]').send_keys(password)
    driver.find_element_by_css_selector('[name="create_account"]').click()
    driver.find_element(By.LINK_TEXT, 'Logout').click()
#
    get_login(driver, email, password)
    driver.find_element(By.LINK_TEXT, 'Logout').click()


def get_login(driver, email, password):
    driver.find_element_by_css_selector('[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('[name="password"]').send_keys(password)
    driver.find_element_by_css_selector('[name="login"]').click()
