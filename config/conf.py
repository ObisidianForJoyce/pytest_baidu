import os

from selenium.webdriver.common.by import By


class ConfigManager(object):
    """
    在这个文件中我们可以设置自己的各个目录，也可以查看自己当前的目录。

    遵循了约定：不变的常量名全部大写，函数名小写。看起来整体美观。
    """

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # logging level
    log_name = 'ui automation.txt'
    level = 'DEBUG'

    # logging path
    # 初始路径
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Logs文件目录地址
    logs_path = os.path.join(dir_path, 'Logs/')
    # report测试报告路径
    report_path = os.path.join(dir_path, 'report/')
    # error screenshots path
    screenshots_path = os.path.join(dir_path, 'attachment/')
    # test cases path
    case_name = os.path.join(dir_path, 'testcases/')

    # 测试网址
    BAIDU_URL = "https://www.baidu.com"
    ZHUIFENG = "https://exam.wzzz.fun"
    WPS_LOGIN = "https://account.wps.cn/"
    FILE_UPLOAD = "https://letcode.in/file"
    WMS_URL = "http://192.168.10.129/login?redirect=%2Findex"
    WHOLE_PATH = "./screenshots/简单验证码.png"
    CROP_PATH = "./screenshots/crop_pic.png"

    # accounts
    USERNAME = "admin"
    PASSWORD = "123456"