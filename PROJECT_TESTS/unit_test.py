import unittest
from selenium import webdriver


class NewClientTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn("PROJECT", self.browser.title)



if __name__ == "__main__":
    unittest.main(warnings="ignore")