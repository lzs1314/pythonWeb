#@coding  :utf-8
#@FileName: logging-main.py
#@Author  :辰晨
#@Time    :2019/4/17 17:33

import logging
#  拿到 Logger对象
logger = logging.getLogger()
# 创建一个handler，用于写入日志文件 文件对象
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台  屏幕对象
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

import turtle as t
t.color("red")
for i in range(300):
	t.fd(i)
	t.left(70)
t.done()

