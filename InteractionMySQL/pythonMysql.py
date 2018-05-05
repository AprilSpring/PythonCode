# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:57:26 2018

@author: Administrator
"""

#6. Python与mysql交互(python script)

#1) mysql数据导入到python
import pandas
from sqlalchemy import creat_engine
engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/cp') #"mysql+mysqlconnector://用户名:密码@IP地址:端口号/数据库名"
data = pandas.read_sql("select * from news;",con=engine)


#2)python数据导入到mysql
from pandas import DataFrame;
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/cp')
data = DataFrame({'age':[21,22,23],'name':['KEN','大数据分析实战','小蚊子']})
data.to_sql("testTable",index=False,con=engine,if_exists='append')



#%% MySQLdb
#http://www.runoob.com/python/python-mysql.html
import MySQLdb

#install
$ gunzip MySQL-python-1.2.2.tar.gz
$ tar -xvf MySQL-python-1.2.2.tar
$ cd MySQL-python-1.2.2
$ python setup.py build
$ python setup.py install

#已经创建了数据库cp中的score表，字段为sid,student_id,corse_id,number













