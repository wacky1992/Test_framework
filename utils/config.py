import os
from utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
PIC_PATH = os.path.join(BASE_PATH, 'pic')
ORIGIN_IMGS_PATH = os.path.join(BASE_PATH, 'origin_imgs')
CLEAN_IMGS_PATH = os.path.join(BASE_PATH, 'clean_imgs')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)