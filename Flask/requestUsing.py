#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:03:16 2019

@author: liutingting16
"""

#%% test1
#from flask import Flask,request
#
#app = Flask(__name__)
#
#@app.route('/login')
#def login():
#    uname = request.form.get("name")
#    return uname
#
#if __name__=="__main__":
#    #app.run(host="127.0.0.1",port="80",debug=True) ##app.run(host='ip', port='端口')
#    app.run()


#%% test2
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search/')
def search():
    l = request.args.get('q')
    return '用户提交的参数是: %s' % l

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        print('username:', username)
        print('password', password)
        return 'login get success'
        #return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username:', username)
        print('password', password)
        return 'login success'


if __name__ == '__main__':
    app.run(debug=True)

#1）GET 请求 ：通过"flask.request.args"来获取
#2）POST 请求 ：通过"flask.reques.form"来获取


#%% test3 - 可执行
#from flask import Flask, render_template, request
# 
#app = Flask(__name__)
# 
# 
#@app.route('/')
#def index():
#    print(type(request.query_string))
#    return render_template('frame.html')
# 
# 
#@app.route('/', methods=['POST'])
#def post():
#    if request.form['name'] == 'a' and request.form['password'] == 'a':
#        return '欢迎' + request.form['name']
#    else:
#        return '用户名密码错误'
# 
#app.run()

