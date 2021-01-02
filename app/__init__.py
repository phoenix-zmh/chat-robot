#!/usr/bin/env python
# encoding: utf-8
'''
@author: yida.hu
@contact: huyidada@163.com
@time: 1/3/21 12:01 AM
@desc:
'''
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask

from app.configs import Config as LogConfig
from app.configs.dev import DevelopementConfig
from app.configs.prop import ProductionConfig

config = {
    "dev": DevelopementConfig,
    "prop": ProductionConfig,
}


def init_app(config_name):
    """项目的初始化函数"""
    app = Flask(__name__)
    # 启用日志功能
    setup_log(LogConfig)

    # 设置配置类
    Config = config[config_name]
    # 加载配置
    app.config.from_object(Config)
    return app


# 把日志相关的配置封装成一个日志初始化函数
def setup_log(Config):
    # 设置日志的记录等级
    logging.basicConfig(level=Config.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    log_path = "logs"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    file_log_handler = RotatingFileHandler(os.path.join(log_path, 'log'), maxBytes=1024 * 1024 * 300, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaskapp使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
