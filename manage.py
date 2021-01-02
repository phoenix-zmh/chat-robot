#!/usr/bin/env python
# encoding: utf-8
'''
@author: yida.hu
@contact: huyidada@163.com
@time: 1/3/21 12:00 AM
@desc:
'''

from app import init_app
import os

app = init_app(os.getenv('DOCKERENV', 'dev'))

from admin import admin

app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
