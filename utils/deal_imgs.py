
def get_crop_imgs(img):
    """
    按照图片的特点,进行切割,这个要根据具体的验证码来进行工作. # 见原理图
    :param img:
    :return:
    """
    child_img_list = []
    for i in range(4):
        x = 2 + i * (6 + 4)  # 见原理图
        y = 0
        child_img = img.crop((x, y, x + 6, y + 10))
        child_img_list.append(child_img)

    return child_img_list