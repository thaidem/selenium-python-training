import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
#    options = webdriver.ChromeOptions()
#    options.add_argument("start-maximized")
#    wd = webdriver.Chrome(chrome_options=options)
#    wd = webdriver.Chrome()
    wd = webdriver.Ie()
    wd.implicitly_wait(20)
#    wd = webdriver.Firefox()
#    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
#    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox ESR\\firefox.exe",
#                           capabilities={"marionette": False})
    request.addfinalizer(wd.quit)
    return wd


def test_get_login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
