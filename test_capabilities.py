import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_capabilities(driver):
    pass
