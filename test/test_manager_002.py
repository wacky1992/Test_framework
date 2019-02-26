import time
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH,PIC_PATH
from utils.log import logger
from utils.file_reader import ExeclReader
from utils.HTMLTestRunner import HTMLTestRunner
from PIL import Image
import pytesseract
import urllib


class TestManager(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_1 = (By.ID,'loginType')
    locator_2 = (By.XPATH,'//*[@id="loginType"]/option[2]')
    locator_3 = (By.ID,'userId')
    locator_4 = (By.ID,'password')
    locator_5 = (By.ID,'pictureRand')
    locator_6 = (By.ID,'code_img')
    locator_7 = (By.NAME,'button')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_1).click()
        self.driver.find_element(*self.locator_2).click()
        self.driver.find_element(*self.locator_3).send_keys('18551765121')
        self.driver.find_element(*self.locator_4).send_keys('liu1992')
