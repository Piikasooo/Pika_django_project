from selenium import webdriver
import pytest
import time


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_title(browser):
    time.sleep(3)
    browser.get('http://127.0.0.1:8000/')
    header_text = browser.find_element_by_tag_name('h1').text
    input_box = browser.find_element_by_id("test_placeholder")
    input_box.send_keys("Hello world")
    time.sleep(3)

    assert header_text == "Pikasooo"
    assert browser.title == "PROJECT"