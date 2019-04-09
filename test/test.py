import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, PIC_PATH, REPORT_PATH
from utils.deal_imgs import deal_pic
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner


class TestRenting(unittest.TestCase):
    URL = Config().get('RetingURL')
    locator_username = (By.XPATH, '/html/body/div/div/div/div[2]/ul/li[2]/p/input')
    locator_password = (By.XPATH, '/html/body/div/div/div/div[2]/ul/li[3]/p/input')
    locator_code = (By.XPATH, '//*[@id="inputCode"]')

    def sub_setup(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.driver.maximize_window()
        pic = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li[4]/div/img')
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" + "001.png")
        x = pic.location['x']
        y = pic.location['y']
        left = pic.size['width'] + x
        right = pic.size['height'] + y
        self.vcode = deal_pic(x, y, left, right)

    def sub_tearDown(self):
        self.driver.quit()

# 测试用例1：测试登录模块
    def test_search_0(self):
        self.sub_setup()
        self.driver.find_element(*self.locator_username).send_keys('18788888888')
        self.driver.find_element(*self.locator_password).send_keys('12345a')
        self.driver.find_element(*self.locator_code).send_keys(self.vcode)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/ul/li[5]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/ul/li[5]/div/button').click()
        time.sleep(5)
            # links = self.driver.find_elements(*self.locator_result)
            # for link in links:
            #     logger.info('成功')
        self.sub_tearDown()

# 测试用例2：测试登录异常
    def test_search_1(self):
        self.sub_setup()
        self.driver.find_element(*self.locator_username).send_keys('18000020001')
        self.driver.find_element(*self.locator_password).send_keys('19921203a')
        self.driver.find_element(*self.locator_code).send_keys(self.vcode)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/ul/li[5]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/ul/li[5]/div/button').click()
        time.sleep(5)
#             # links = self.driver.find_elements(*self.locator_result)
#             # for link in links:
        logger.info('成功')
        self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(TestRenting))
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 测试', description='修改html报告')
        runner.run(testunit)
