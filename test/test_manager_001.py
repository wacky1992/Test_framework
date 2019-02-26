import time
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH,PIC_PATH
from utils.log import logger
from utils.file_reader import ExeclReader
from utils.HTMLTestRunner import HTMLTestRunner
import os


def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time

class TestManager(unittest.TestCase):
    URL = Config().get('URL')
    '''数据分析模块'''
    locator_data_analysis = (By.ID,'296')
    '''统计报表'''
    locator_report_001 = (By.ID,'213')
    '''设备月统计'''
    locator_report_002 = (By.ID,'297')
    '''设备日明细'''
    locator_report_003 = (By.ID,'304')
    '''设备月明细'''
    locator_report_004 = (By.ID,'319')
    '''日在线数据补录'''
    locator_report_005 = (By.ID,'451')
    '''数据报表补录'''
    locator_report_006 = (By.ID,'475')
    '''场所历史离线查询'''
    locator_report_007 = (By.ID,'485')
    '''上下线日志'''
    locator_report_008 = (By.ID,'232')
    '''虚拟身份上下线'''
    locator_report_009 = (By.ID,'255')
    '''虚拟身份上线'''
    locator_report_010 = (By.ID,'254')





    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_select_0(self):
        time.sleep(10)
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_001).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "统计报表" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_1(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_002).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "设备月统计" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_2(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_003).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "设备日明细" + time_format() + ".png")
        self.sub_tearDown()


    def test_select_3(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_004).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "设备月明细" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_4(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_005).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "日在线数据补录" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_5(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_006).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "数据报表补录" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_6(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_007).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "场所历史离线查询" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_7(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_008).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "上下线日志" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_8(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_009).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "虚拟身份上下线" + time_format() + ".png")
        self.sub_tearDown()

    def test_select_9(self):
        self.driver.find_element(*self.locator_data_analysis).click()
        self.driver.find_element(*self.locator_report_010).click()
        time.sleep(2)
        links = ("正常点击")
        for link in links:
            logger.info(link.text)
        self.driver.get_screenshot_as_file(PIC_PATH + "\\" +  "虚拟身份上线" + time_format() + ".png")
        self.sub_tearDown()






if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 测试', description='修改html报告')
        runner.run(TestBaiDu('test_search_0'))