from selenium import webdriver
"""
    配置浏览器的options用以加快用例执行速度。
"""

def options1():
    options = webdriver.ChromeOptions()
    # 窗体最大化
    options.add_argument('start-maximized')
    # 无头模式
    #options.add_argument('--headless')

    options.add_argument('--log_level=3')  # 设置 Chrome 浏览器的日志级别
    '''
        --log_level=3 日志级别
        在生产环境中，一般建议将日志级别设置为较低的级别（如 3）以减少日志量。而在开发和调试过程中，你可能需要更详细的日志信息，可以将日志级别设置得更高（如 1）
        0：DEFAULT，使用默认日志记录级别。
        1：VERBOSE，输出详细的日志信息，包括调试信息。
        2：INFO，输出一般的信息级别日志。
        3：WARNING，输出警告级别的日志。
        4：ERROR，输出错误级别的日志。
        5：FATAL，输出严重错误级别的日志。
    '''
    # 返回options对象
    return options