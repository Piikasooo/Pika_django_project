from selenium import webdriver

def test():
    browser = webdriver.Chrome()
    browser.get('http://127.0.0.1:8000/')

    print(browser.title)

    assert browser.title == "PROJECT"