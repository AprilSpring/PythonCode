# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:41:15 2018

@author: User
"""

# pandas learning
import pandas as pd
from pandas import Series,DataFrame


#%% Series操作
#1.数组生成series
x = Series([1,2,3,4])
x.values
x.index

x = Series([1, 2, 3, 4], index = ['a', 'b', 'd', 'c']) #指定index的series
x[['c','a','b']] #通过index进行取值
x[x>2]

type(x)

#2.字典生成series
data = {'a':1, 'b':2, 'd':3, 'c':4}
x = Series(data)

exindex = ['a', 'b', 'c', 'e'] #指定额外index
y = Series(data, index = exindex)

x+y #相同索引值行相加，不同行索引则数值为NaN'

y.name = 'weight of letters' #指定series名字
y.index.name = 'letter' #指定index名字



#%% DataFrame操作
#dataframe的每行每列都是series

#1.字典生成dataframe
data = {'state':['ok', 'ok', 'good', 'bad'],
        'year':[2000, 2001, 2002, 2003],
        'pop':[3.7, 3.6, 2.4, 0.9]}
x = pd.DataFrame(data)
x['state'] #返回名为state的series
x.state
x['debt'] = 16.5 #修改整列数据值
x['y'] = [1,1,0,1] #新增一列值，命名为y

#iloc是根据位置选择，需要用数字
#loc是根据名称选择，需要用索引名称
data[:3] #取前3行
data.iloc[0:3] #取前3行
data.iloc[0:3,1] #取前3行，第2列
data.columns.size #计算data的列数目
data.iloc[:,0].size #计算data的行数目
data['y'].isin([1]) #返回True or False，相当于R语言which的功能
data[data['y'].isin([1])] #返回所有y列是1的行
data[data['y'].isin([0])]
data.shape #查看数据维度



#%% 文件读入

#1.read_csv
data = pd.read_csv(file='./aaa.txt',sep='\t', header=None, names=['A', 'B'],index_col=1)
#index_col=1 按照第一列进行索引
#prefix='X' 在没有列标题时，给列添加前缀。例如：添加‘X’ 成为 X0, X1, …

#2.read_table
data = pd.read_table('TEST.csv', names=['A', 'B'])

#3.写入到csv
t1.to_csv(outname, index=False, names = ['A', 'B'])

#4.写入到Excel
t1.to_excel()



#%% 其他常用小函数

#数据转换和补充
astype()
replace()
dropna()
notnull()
df['key1'].fillna(0)
X[‘age’].fillna(X[‘age’].mean(),inplace=True)
df.rename(columns={'data1':'a','data2':'b','key1':'c','key2':'d'}) #修改df列名

#数据查询
X['age']
X[[‘age’,’sex’,’name’]]
X.loc[X[‘type’] == 0][[‘age’,’sex’]]
X.iloc[0:3,0:3]
X[::-1] #将X进行反序
X.info()
X[:3]
X.head() #data是dataframe格式
X.tail()
np.where(results == results.max())[0]
np.where(df['key1'].str.contains('Windows'), 'Windows', 'Not Windows')

#数据分组
df['data1'].groupby(df['key1']).mean() #根据key1，对data1进行分组，并求每组均值
df.groupby(['year','sex'])
np.allclose(df.groupby(['year', 'sex']).prop.sum(), 1) #验证所有分组prop的总和是否为1

#数据统计
df['key1'].value_counts()
df['key1'].apply(lambda x: len(x.split(';')))

#数据排序
df.sort_index(by='key1', ascending=True)

#数据合并
pd.merge()
pd.concat(a,b,ignore_index=True,axis=0) #axis=0按照行合并

#数据透视表 pivot_table, help(pd.pivot_table)
table = pd.pivot_table(df, index=['key1','key2'], columns=['key3'], aggfunc=np.sum)
table = pd.pivot_table(df, index='year', columns='sex', aggfunc=np.sum, fill_value=0) #统计每年、不同性别，出生人数总和

pd.stack()
pd.unstack()

pd.reindex()
pd.reset_index()
pd.set_index()
pd.rename()
























