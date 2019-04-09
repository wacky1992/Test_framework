from utils.config import PIC_PATH
from PIL import Image
import pytesseract


def deal_pic(x, y, left, right):
        with Image.open(PIC_PATH + "\\" + "001.png") as im:
                img = im.crop((x, y, left, right))
                img.save(PIC_PATH + "\\" + "001-1.png")
                im.close()
                img.close()

        with Image.open(PIC_PATH + "\\" + "001-1.png") as img_pic:
                imgry = img_pic.convert('L')  # 转灰度
                vcode = pytesseract.image_to_string(imgry)
                img_pic.close()
                imgry.close()

        return vcode