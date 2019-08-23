import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_sign_login(driver):
    driver.get("https://litecart.stqa.ru/en/")
    # driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector('table a').click()
    driver.find_element_by_css_selector('[name="firstname"]').send_keys("Dmitry")
    driver.find_element_by_css_selector('[name="lastname"]').send_keys("Kozlov")
    driver.find_element_by_css_selector('[name="address1"]').send_keys("5-24 49th Ave Apt.1 Long Island City")
    driver.find_element_by_css_selector('[name="postcode"]').send_keys("11101")
    driver.find_element_by_css_selector('[name="city"]').send_keys("New York")
    # countries = driver.find_element_by_css_selector('select')
    # driver.execute_script("arguments[0].setAttribute('aria-hidden', 'false')", countries)
    driver.find_element_by_css_selector('.select2-selection').click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, './select[@name="country_code"]
    # /option[[value="US"]')))
    driver.find_element_by_css_selector('input.select2-search__field')\
        .send_keys("United States" + Keys.ENTER)
    # countries.find_element_by_css_selector('select [value="US"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('[value="NY"]').click()
    driver.find_element_by_css_selector('[name="email"]').send_keys("thaidem197@gmail.com")
    driver.find_element_by_css_selector('[name="phone"]').send_keys(Keys.HOME + "+1-910-336-0370")
    driver.find_element_by_css_selector('[name="password"]').send_keys("260596")
    driver.find_element_by_css_selector('[name="confirmed_password"]').send_keys("260596")
    driver.find_element_by_css_selector('[name="create_account"]').click()
    driver.find_element(By.LINK_TEXT, 'Logout').click()
#
    driver.find_element_by_css_selector('[name="email"]').send_keys("thaidem197@gmail.com")
    driver.find_element_by_css_selector('[name="password"]').send_keys("260596")
    driver.find_element_by_css_selector('[name="login"]').click()
    driver.find_element(By.LINK_TEXT, 'Logout').click()
