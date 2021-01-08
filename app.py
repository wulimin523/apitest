# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :app
# @Date     :2020/12/28 10:35
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import os
import logging.handlers
import time
# 当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "https://xt.hbgf.net.cn/hours/"
HEADERS = {"Content-Type":"application/json"}
TOKEN = ""

# 日志模块设置方法
def init_logging():
    # 初始化日志器
    logger = logging.getLogger()
    # 添加注释
    print('我是利民')

    # 初始化处理器
    # 控制台
    sh = logging.StreamHandler()
    # 文件
    all_log_dir =BASE_DIR + '/log/all_logs'
    error_log_dir =BASE_DIR + '/log/error_logs'
    if not os.path.exists(all_log_dir):
        os.mkdir(all_log_dir)
    if not os.path.exists(error_log_dir):
        os.mkdir(error_log_dir)
    now_time = time.strftime("%Y%m%d_%H%M%S")
    fh_a = logging.handlers.TimedRotatingFileHandler(filename=all_log_dir+'/{}.log'.format(now_time),
                                                   when='s',
                                                   interval=5,
                                                   backupCount=4,
                                                   encoding='utf-8')
    fh_e = logging.handlers.TimedRotatingFileHandler(filename=error_log_dir+'/{}.log'.format(now_time),
                                                    when='s',
                                                    interval=5,
                                                    backupCount=4,
                                                    encoding='utf-8' )
    # 初始化格式器
    fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d - %(message)s"
    formatter = logging.Formatter(fmt=fmt)

    # 格式器添加到处理器
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)
    fh_a.setFormatter(formatter)
    fh_a.setLevel(logging.DEBUG)
    fh_e.setFormatter(formatter)
    fh_e.setLevel(logging.ERROR)
    # 处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh_a)
    logger.addHandler(fh_e)

