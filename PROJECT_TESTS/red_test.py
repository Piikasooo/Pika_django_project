from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_title(browser):
    browser.get('http://127.0.0.1:8000/')
    assert browser.title == "PROJECT"