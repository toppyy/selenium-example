from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



class Browser():
    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()
    def get(self, url):
        try:
            self.driver.get(url)
        except Exception as ex:
            print(ex.msg)
    def find(self,by_what, what_to_find):
        try:
            el = self.driver.find_element(by_what, what_to_find)
            return el
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    def find_many(self,by_what, what_to_find):
        try:
            el = self.driver.find_elements(by_what, what_to_find)
            return el
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_find(self, url, by_what, what_to_find):
        try:
            self.driver.get(url)
            el = self.driver.find_element(by_what, what_to_find)
            return el
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    def get_source(self):
        return self.driver.page_source