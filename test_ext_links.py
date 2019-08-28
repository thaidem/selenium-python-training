import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # wd = webdriver.Ie()
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_ext_links(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
#
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country")
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    all_links = driver.find_elements_by_css_selector('.fa-external-link')
    for link in all_links:
        link.click()
        current_windows = driver.window_handles
        print(current_windows)
        for new_window in current_windows:
            if new_window != main_window:
                wait.until(EC.new_window_is_opened(old_windows))
                driver.switch_to_window(new_window)
                print(driver.current_window_handle)
                driver.close()
                driver.switch_to_window(main_window)
                print(driver.current_window_handle)
