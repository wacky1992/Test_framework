import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID,'kw')
    locator_su = (By.ID,'su')
    locator_result = (By.XPATH,'//*[@id="container"]/div[2]/div/div[2]/span')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

if __name__ == '__main__':
    unittest.main()