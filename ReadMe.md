v0.1版本使用说明：
1、软件版本说明：建议使用python3.5.2版本（此版本可以正确引用pyyaml模块）、使用的chromewebdriver适用于67.0版本、次项目使用pycharm编写。
2、需要的python第三方库：selenium、pyyaml、xlrd、xlwt
3、日志以及文件配置查看config.yml文件，请在test文件夹下编写自动化脚本，具体修改请查看之前的脚本。



目录以及函数说明：
|-framework                 根目录
  |-config/                 配置文件
    |-config.yml            日志、网址等配置信息文件
  |-data/                   导入数据内容
    |-***.xlsx              输入参数
  |-driver/                 浏览器启动器
    |-chromedriver.exe
  |-log/                    日志文件
  |-pic/                    保存验证码图片
  |-report/                 报告文件
    |-***.html
  |-test/                   测试用例套
    |-test_***.py
  |-utils/                  项目主函数
    |-config.py             路径配置
    |-file_reader.py        文件提取处理
    |-HTMLTestRunner.py     测试报告模板
    |-log.py                日志配置
    |-deal_imgs.py          处理验证码






备注：windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini
文件内容：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
timeout = 150