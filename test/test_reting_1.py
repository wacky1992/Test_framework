import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from utils.log import logger


class TestReting(unittest.TestCase):
    URL = Config().get('RetingRUL')
    locator_username = (By.XPATH, '/html/body/div/div/div/div[2]/ul/li[2]/p/input')
    locator_password = (By.XPATH, '/html/body/div/div/div/div[2]/ul/li[3]/p/input')
    locator_
