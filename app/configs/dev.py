#!/usr/bin/env python
# encoding: utf-8
'''
@author: yida.hu
@contact: huyidada@163.com
@time: 1/3/21 12:31 AM
@desc:
'''
from . import Config


class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True
