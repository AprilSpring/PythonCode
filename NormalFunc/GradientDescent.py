# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:00:33 2018

@author: User
"""

# Gradient Descent Learning
# https://www.2cto.com/net/201610/557111.html 
import numpy as np
import random

#%% 1.Batch Gradient Descent
#用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出
#input1  1   2   5   4
#input2  4   5   1   2
#output  19  26  19  20
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
y = [19,26,19,20]   #输出
theta = [1,1]       #θ参数初始化
loss = 10           #loss先定义一个数，为了进入循环迭代
step_size = 0.01    #步长
eps =0.0001         #精度要求
max_iters = 10000   #最大迭代次数
error =0            #损失值
iter_count = 0      #当前迭代次数
 
err1=[0,0,0,0]      #求Θ1梯度的中间变量1
err2=[0,0,0,0]      #求Θ2梯度的中间变量2
 
while( loss > eps and iter_count < max_iters):   #迭代条件：误差足够小or达到迭代次数
    loss = 0
    err1sum = 0
    err2sum = 0
    for i in range (4):     #每次迭代所有的样本都进行训练
        pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1]  #预测值
        err1[i]=(pred_y-y[i])*input_x[i][0]
        err1sum=err1sum+err1[i]
        err2[i]=(pred_y-y[i])*input_x[i][1]
        err2sum=err2sum+err2[i]
    theta[0] = theta[0] - step_size * err1sum/4  #对应5式
    theta[1] = theta[1] - step_size * err2sum/4  #对应5式
    for i in range (4):
        pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1]   #预测值
        error = (1/(2*4))*(pred_y - y[i])**2  #损失值
        loss = loss + error  #总损失值
    iter_count += 1
    print ("iters_count", iter_count)
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)


#%% 1.2 向量化形式
# y = X*Θ
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
input_x = np.matrix(input_x) #4*2
y = [19,26,19,20]   #输出
y = np.matrix(y).T #4*1
theta = [1,1]       #θ参数初始化
theta = np.matrix(theta).T #2*1
loss = 10           #loss先定义一个数，为了进入循环迭代
step_size = 0.01    #步长
eps =0.0001         #精度要求
max_iters = 10000   #最大迭代次数
error =0            #损失值
iter_count = 0      #当前迭代次数
 
while( loss > eps and iter_count < max_iters):
    pred_y = input_x * theta
    err = input_x.T * (pred_y -y)
    theta = theta - step_size * err/input_x.shape[0]  #对应5式
    pred_y = input_x * theta
    loss = (1/(2*input_x.shape[0]))*((pred_y - y).T*(pred_y - y))[0,0]
    iter_count += 1
    print ("iters_count", iter_count)
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)


#%% 1.3 函数化
def gradientDescent2(X, y, theta, alpha, iters):
    input_x = np.matrix(X)
    y = np.matrix(y)
    theta = np.matrix(theta).T #2*1
    loss = 10           #loss先定义一个数，为了进入循环迭代
    eps = 0.0001         #精度要求
    iter_count = 0      #当前迭代次数
    while( loss > eps and iter_count < iters):
        pred_y = input_x * theta
        err = input_x.T * (pred_y -y)
        theta = theta - alpha * err/input_x.shape[0]
        pred_y = input_x * theta
        loss = (1/(2*input_x.shape[0]))*((pred_y - y).T*(pred_y - y))[0,0] #cost function
        iter_count += 1
        #print ("iters_count", iter_count)
    #print ('theta: ',theta )
    #print ('final loss: ', loss)
    #print ('iters: ', iter_count)
    return theta.T, loss

g, cost = gradientDescent2(input_x, y, theta, alpha=0.01, iters=1000)


#%% 1.4 直接使用sklearn模块计算预测结果
'''
备注：
sklearn.linear_model.LinearRegression求解线性回归方程参数时，
首先判断训练集X是不是稀疏矩阵，如是，就用Golub & Kahan双对角线化过程方法来求解；
否则就调用C库LAPACK中的用基于分治法的奇异值分解来求解,
这些解法都跟梯度下降没有半毛钱的关系。
'''
from sklearn import linear_model
model = linear_model.LinearRegression() #创建线性回归模型
model.fit(X, y) #X is X_train, y is y_train, 训练集构建模型
f = model.predict(X).flatten() #X is X_test, 测试集预测结果
model.score(X,y) #X is X_test, y is y_test, 测试集预测结果的优劣得分


#%% 2.Stochastic Gradient Descent
#用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出
#input1  1   2   5   4
#input2  4   5   1   2
#output  19  26  19  20
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
y = [19,26,19,20]   #输出
theta = [1,1]       #θ参数初始化
loss = 10           #loss先定义一个数，为了进入循环迭代
step_size = 0.01    #步长
eps =0.0001         #精度要求
max_iters = 10000   #最大迭代次数
error =0            #损失值
iter_count = 0      #当前迭代次数
 
while( loss > eps and iter_count < max_iters):    #迭代条件
    loss = 0
    i = random.randint(0,3)  #每次迭代在input_x中随机选取一组样本进行权重的更新
    pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1] #预测值
    theta[0] = theta[0] - step_size * (pred_y - y[i]) * input_x[i][0]
    theta[1] = theta[1] - step_size * (pred_y - y[i]) * input_x[i][1]
    for i in range (3):
        pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1] #预测值
        error = 0.5*(pred_y - y[i])**2
        loss = loss + error
    iter_count += 1
    print ('iters_count', iter_count)
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)


#%% 2.2 向量化形式
# y = X*Θ
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
input_x = np.matrix(input_x) #4*2
y = [19,26,19,20]   #输出
y = np.matrix(y).T #4*1
theta = [1,1]       #θ参数初始化
theta = np.matrix(theta).T #2*1
loss = 10           #loss先定义一个数，为了进入循环迭代
step_size = 0.01    #步长
eps =0.0001         #精度要求
max_iters = 10000   #最大迭代次数
error =0            #损失值
iter_count = 0      #当前迭代次数

while( loss > eps and iter_count < max_iters):
    i = random.randint(0,input_x.shape[0]-1) #随机选择一组样本
    input_x1 = input_x[i] #1*2
    y1 = y[i] #1*1
    pred_y = input_x1 * theta
    err = input_x1.T * (pred_y -y1)
    theta = theta - step_size * err/input_x1.shape[0]  #对应5式
    pred_y = input_x * theta
    loss = (1/(2*input_x.shape[0]))*((pred_y - y).T*(pred_y - y))[0,0]
    iter_count += 1
    print ("iters_count", iter_count)
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)


#%% 3.Mini-Batch Gradient Descent
#用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出
#input1  1   2   5   4
#input2  4   5   1   2
#output  19  26  19  20
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
y = [19,26,19,20]       #输出
theta = [1,1]           #θ参数初始化
loss = 10               #loss先定义一个数，为了进入循环迭代
step_size = 0.01        #步长
eps =0.0001             #精度要求
max_iters = 10000       #最大迭代次数
error =0                #损失值
iter_count = 0          #当前迭代次数
 
 
while( loss > eps and iter_count < max_iters):  #迭代条件
    loss = 0
    #这里每次批量选取的是2组样本进行更新，另一个点是随机点+1的相邻点
    i = random.randint(0,3)     #随机抽取一组样本
    j = (i+1)%4                 #抽取另一组样本，j=i+1
    pred_y0 = theta[0]*input_x[i][0]+theta[1]*input_x[i][1]  #预测值1
    pred_y1 = theta[0]*input_x[j][0]+theta[1]*input_x[j][1]  #预测值2
    theta[0] = theta[0] - step_size * (1/2) * ((pred_y0 - y[i]) * input_x[i][0]+(pred_y1 - y[j]) * input_x[j][0])  #对应5式
    theta[1] = theta[1] - step_size * (1/2) * ((pred_y0 - y[i]) * input_x[i][1]+(pred_y1 - y[j]) * input_x[j][1])  #对应5式
    for i in range (3):
        pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1]     #总预测值
        error = (1/(2*2))*(pred_y - y[i])**2                    #损失值
        loss = loss + error       #总损失值
    iter_count += 1
    print ('iters_count', iter_count)
 
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)


#%% 3.2 向量化形式
# y = X*Θ
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入
input_x = np.matrix(input_x) #4*2
y = [19,26,19,20]   #输出
y = np.matrix(y).T #4*1
theta = [1,1]       #θ参数初始化
theta = np.matrix(theta).T #2*1
loss = 10           #loss先定义一个数，为了进入循环迭代
step_size = 0.01    #步长
eps =0.0001         #精度要求
max_iters = 10000   #最大迭代次数
error =0            #损失值
iter_count = 0      #当前迭代次数

while( loss > eps and iter_count < max_iters):
    i = random.randint(0,input_x.shape[0]-1) #随机选择一组样本
    j = (i+1)%4 #随机选择另外一组样本
    input_x1 = input_x[i] #1*2
    y1 = y[i] #1*1
    input_x2 = input_x[j] #1*2
    y2 = y[j]
    pred_y1 = input_x1 * theta
    pred_y2 = input_x2 * theta
    err = input_x1.T * (pred_y1 -y1) + input_x2.T * (pred_y2 -y2)   #计算2组样本的错误率和
    theta = theta - step_size * err/(input_x1.shape[0]+input_x2.shape[0])  #对应5式
    pred_y = input_x * theta
    loss = (1/(2*input_x.shape[0]))*((pred_y - y).T*(pred_y - y))[0,0]
    iter_count += 1
    print ("iters_count", iter_count)
print ('theta: ',theta )
print ('final loss: ', loss)
print ('iters: ', iter_count)

