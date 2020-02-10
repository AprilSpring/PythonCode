#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:48:39 2019

Flask学习

@author: liutingting16
"""

#%% test1
#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/hello')
#def hello_world():
#    return 'Hello World!'
#
#if __name__ == '__main__':
#    app.run()

 
# 执行python hello.py
# 打开网页 http://127.0.0.1:5000/hello 显示“Hello World!”  


#%% test2
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"    

if __name__ == '__main__':
    app.run()    

# 两个链接http://127.0.0.1:5000 和 http://127.0.0.1:5000/index 都指向hello world

