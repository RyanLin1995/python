# 正常的日志格式

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %('
                           'levelname)s:%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.debug("This is a debug")
logging.info("This is a info")
logging.warning("This is a warning")
logging.error("This is a error")
logging.critical("This is a critical")