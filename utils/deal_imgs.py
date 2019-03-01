from selenium import webdriver
import os
from utils.config import PIC_PATH, Config
from PIL import Image
import pytesseract


def deal_pic():
        URL = Config().get('RetingURL')
        base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
        driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get(URL)
        driver.maximize_window()
        pic = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li[4]/div/img')
        driver.get_screenshot_as_file(PIC_PATH + "\\" + "001.png")
        x = pic.location['x']
        y = pic.location['y']
        left = pic.size['width'] + x
        right = pic.size['height'] + y
        im = Image.open(PIC_PATH + "\\" + "001.png")
        img = im.crop((x, y, left, right))
        img.save(PIC_PATH + "\\" + "001-1.png")
        img_pic = Image.open(PIC_PATH + "\\" + "001-1.png")
        imgry = img_pic.convert('L')  # 转灰度
        vcode = pytesseract.image_to_string(imgry)
        return vcode




