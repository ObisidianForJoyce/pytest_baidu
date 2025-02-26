import logging
import os

from config.conf import ConfigManager

log_path_name = os.path.join(ConfigManager.logs_path, ConfigManager.log_name)


class LogHandle(logging.Logger):
    """定义日志类"""

    def __init__(self, name, file, level='DEBUG',
                 fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"):
        super().__init__(name)
        self.setLevel(level)

        file_headers = logging.FileHandler(file)
        file_headers.setLevel(level)
        self.addHandler(file_headers)
        fmt = logging.Formatter(fmt)
        file_headers.setFormatter(fmt)


logger = LogHandle(ConfigManager.log_name, log_path_name, level=ConfigManager.level)

if __name__ == '__main__':
    log = logger
    log.warning('测试1')
