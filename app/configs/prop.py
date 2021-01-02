#!/usr/bin/env python
# encoding: utf-8
'''
@author: yida.hu
@contact: huyidada@163.com
@time: 1/3/21 12:32 AM
@desc:
'''
from . import Config


class ProductionConfig(Config):
    """生产模式下的配置"""
    DEBUG = False
