# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:43:35 2018

@author: Administrator
"""

# numpy learning
import numpy as np


#索引查询：where
cluster1 = X[np.where(idx == 0)[0],:] #查询idx等于i的索引

#随机向量
np.random.randint(0, 4, 10) #随机初始化一个值在0-4之间、长度为10的向量
np.random.random([2,3]) #随机产生值在[0-1]间的2*3矩阵

#奇异值分解svd
X = np.matrix(X) #先转换成numpy matrix，才可以使用向量化形式处理数据
cov = (X.T * X) / X.shape[0] #计算协方差矩阵
U, S, V = np.linalg.svd(cov) #奇异值分解

#数学运算
np.sqrt(1024) #返回幂指数32，即2^32
np.power(2,3) #等同于2**3
np.exp(2) #e^2
np.log([2,4,8]) #自然对数,以e为底
np.log2([2,4,8])

#求和
a = np.array([[[1,2,3,2],[1,2,3,1],[2,3,4,1]],[[1,0,2,0],[2,1,2,0],[2,1,1,1]]])
np.sum(a) #所有值相加
np.sum(a,axis=0) #对应位置相加，相当于sum(a)
np.sum(a,axis=1) #列和
np.sum(a,axis=2) #行和

#乘法
a = np.array([[1, 2, 3], [4, 5, 6]]) #2*3
b = np.array([[1, 2], [3, 4], [5, 6]]) #3*2
c = b #3*2
np.dot(a,b) #求内积，相当于b'*a，2*2
np.dot(a,a) #等同于 a.T @ a
np.multiply(b,c) #对应元素相乘，等同于b*c，3*2

#逻辑与或非
np.logical_and(True, False)#False
np.logical_and([True, False], [False, False])#[False,False]
np.logical_or(True, False)
np.logical_or([True, False], [False, False]) #[True,False]
np.logical_not(True) #False
np.logical_not([True,False]) #[False,True]

#数组拼接：concatenate
a=np.array([1,2,3])
b=np.array([11,22,33])
c=np.array([44,55,66])
np.concatenate((a,b,c),axis=0) #对于一维数组拼接，axis的值不影响最后的结果

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,21,31],[7,8,9]])
np.concatenate((a,b),axis=0)
np.concatenate((a,b),axis=1) #axis=1表示对应行的数组进行拼接

#改变向量维度：reshape
a = np.array([0,1,2,3,4,5,6,7])
a.reshape(4,2)
np.reshape(a,(4,2))

#多维数据降成一维数组
arr3 = np.array(((1,3),(2,3),(5,3)))
arr3.ravel()
arr3.flatten()

#向量转换成矩阵形式
np.matrix(arr3)
type(arr3)

np.zeros(3) #array([ 0.,  0.,  0.])

np.unique(data['y']) #查看有几类标签

a = np.array([3, 1, 2, 4, 6, 6, 1])
np.argmax(a) #返回最大值第一次出现所在的索引
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
np.argmax(a, axis=0) #axis=0，按列返回最大值第一次出现所在的索引
np.argmax(a, axis=1) #axis=1，按行返回最大值第一次出现所在的索引
np.argmin()

a = np.array([[1, 1], [2, 2], [3, 3]])
np.insert(a, 1, 5) #不写axis时，按照a的向量形式在1的位置添加元素5
np.insert(a, 1, 5, axis=1) #axis=1，按照a的第2列，添加元素为5的向量
np.insert(a, 1, 5, axis=0) #axis=0，按照a的第2行，添加元素为5的向量
# 区别 a.insert(0, 'Ones', 1) #在第1列的位置，插入列名为Ones、值为1的列


#其他常用函数
np.where(results == results.max())[0]
np.where(df['key1'].str.contains('Windows'), 'Windows', 'Not Windows')
np.where(pd.isnull(a), b, a)
np.size() #m*n
unstack()
argsort()
np.take([4, 3, 5, 7, 6, 8],indices=[0,1,4]) #返回 array([4, 3, 6])
count_subset.div(count_subset.sum(1), axis=0)
np.allclose(df.groupby(['year', 'sex']).prop.sum(), 1) #验证所有分组prop的总和是否为1
cumsum()




















