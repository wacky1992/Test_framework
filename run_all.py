from utils.config import TEST_PATH
import unittest


def all_case():
    discover = unittest.defaultTestLoader.discover(TEST_PATH, pattern="test_baidu_5.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())
