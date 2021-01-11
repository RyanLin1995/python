# 即输出到屏幕也保存到文件的日志格式
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置Log的总等级

# 第二部，创建一个handler用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')  # 打开log文件
fh.setLevel(logging.DEBUG)

# 第三步，再创建一个用于输出到控制台的handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 第四步，定义handler的格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler中
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug("This is a debug")
logger.info("This is a info")
logger.warning("This is a warning")
logger.error("This is a error")
logger.critical("This is a critical")