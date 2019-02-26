import os
import  time
from selenium import webdriver
from selenium.webdriver.common.by import By


def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time


URL = "http://www.baidu.com"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
pic_path = os.path.join(base_path,'pic')


locator_kw = (By.ID,'kw')
locator_su = (By.ID,'su')
locator_result = (By.XPATH,'//*[@id="container"]/div[2]/div/div[2]/span')

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium 测试')
driver.find_element(*locator_su).click()
time.sleep(2)
driver.get_screenshot_as_file(pic_path + "\\" + time_format() + ".png")
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
driver.quit()

