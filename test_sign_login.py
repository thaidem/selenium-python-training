import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    #wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_sign_login(driver):
    driver.get("https://litecart.stqa.ru/en/")
    # driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector('table a').click()
    driver.find_element_by_css_selector('[name="firstname"]').send_keys("Dmitry" + Keys.TAB)
    driver.find_element_by_css_selector('[name="lastname"]').send_keys("Kozlov" + Keys.TAB)
    driver.find_element_by_css_selector('[name="address1"]').send_keys("5-24 49th Ave Apt.1 Long Island City"
                                                                       + Keys.TAB)
    driver.find_element_by_css_selector('[name="postcode"]').send_keys("11101" + Keys.TAB)
    driver.find_element_by_css_selector('[name="city"]').send_keys("New York" + Keys.TAB)
    # print(driver.find_element_by_css_selector('select').text)
    select = (driver.find_element_by_css_selector('select'))
    driver.execute_script("arguments[0].setAttribute('aria-hidden', 'false')", select)
    # driver.execute_script("arguments[0].setAttribute('autofocus', 'true')", select)
    # driver.execute_script("arguments[0].setAttribute('height', '15px')", select)
    # driver.execute_script("arguments[0].setAttribute('width', '15px')", select)
    print(select.find_element_by_css_selector('[select value="US"]').text)
    # select.find_element_by_css_selector('select [value="US"]').click()
    list = select.find_element_by_css_selector('[value="US"]')
    ActionChains(driver).move_to_element(select).click(list).send_keys(Keys.TAB).perform()
    # actions = ActionChains(driver)
    # actions.move_to_element(select)
    # actions.click(list)
    # actions.pause(10)
    # actions.send_keys(Keys.ENTER)
    # actions.click(hidden_menu)
    # actions.send_keys(Keys.TAB)
    # actions.send_keys(Keys.TAB)
    # actions.move_to_element(hidden_menu)
    # actions.click(hidden_menu)
    # actions.perform()
    # ActionChains(driver).click(hidden_menu).perform()
    # ActionChains(driver).move_to_element(select).click().click(hidden_menu).perform()
    # ActionChains(select.find_element_by_css_selector('[value="US"]')).click().send_keys(Keys.TAB).perform()
    # .move_to_element(select).click().click(hidden_menu).send_keys(Keys.TAB).perform()
    pass
