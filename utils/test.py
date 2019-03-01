from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from utils.config import PIC_PATH
from PIL import Image



URL = "https://azb.yzctid.com/renting/#/login"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
wait = WebDriverWait(driver, 10)
driver.get(URL)
driver.maximize_window()
driver.get_screenshot_as_file(PIC_PATH + "\\" + "001.png")
pic = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li[4]/div/img')
x = pic.location['x']
y = pic.location['y']
left = pic.size['width'] + x
right = pic.size['height'] + y
im = Image.open(PIC_PATH + "\\" + "001.png")
img = im.crop((x, y, left, right))
img.save(PIC_PATH + "\\" + "001-1.png")
driver.quit()






#
#
# def parser(url):
#     driver.get(url)
#     driver.maximize_window()
#     html = driver.page_source
#     doc = lxml.html.fromstring(html)
#     print('parser中的doc为')
#     print(doc)
#     return doc
#
#
# def get_main_url():
#     try:
#         doc = parser('https://azb.yzctid.com/renting/#/login')
#         name = doc.xpath('//*[@id="app"]/div/div/div[2]/ul/li[4]/div/img@src')
#         u = doc.xpath('//*[@id="app"]/div/div/div[2]/ul/li[4]/div/img')
#         for item, fileName in zip(u, name):
#             main_url = 'https://azb.yzctid.com/renting/#/login' + item
#             print('主链接已找到' + main_url)
#             if '*' in fileName:
#                 fileName = fileName.replace('*', '')
#     except:
#         pass


