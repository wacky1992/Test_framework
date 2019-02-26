import random
from urllib.request import urlretrieve
import os
from utils.config import Config,ORIGIN_IMGS_PATH

# 下载验证码图片
url = 'http://www.moguproxy.com/proxy/validateCode/createCode?time={}'
path = ORIGIN_IMGS_PATH + '/'

for i in range(1532067398380,1532067408680):
    urlretrieve(url.format(i), path + str(i)[-3:] + '.jpg')
    print('成功下载 {} 张图片'.format(str(i)[-3:]))