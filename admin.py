#!/usr/bin/env python
# encoding: utf-8
'''
@author: yida.hu
@contact: huyidada@163.com
@time: 1/3/21 1:18 AM
@desc:
'''
from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return 'Hello World !'
