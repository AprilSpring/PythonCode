# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:30:29 2018

@author: Administrator
"""

# scipy.optimize learning

#%% 提供了常用的最优化函数
#from scipy import optimize
'''
1.非线性最优化
fmin  --  简单Nelder-Mead算法
fmin_powell --  改进型Powell法
fmin_bfgs  --  拟Newton法
fmin_cg -- 非线性共轭梯度法
fmin_ncg  --  线性搜索Newton共轭梯度法
leastsq  -- 最小二乘

2.有约束的多元函数问题
fmin_l_bfgs_b ---使用L-BFGS-B算法
fmin_tnc  ---梯度信息
fmin_cobyla ---线性逼近
fmin_slsqp ---序列最小二乘法
nnls ---解|| Ax - b ||_2 for x>=0

3.全局优化
anneal  ---模拟退火算法
brute  --强力法

4.标量函数
fminbound
brent
golden
bracket

5.拟合
curve_fit-- 使用非线性最小二乘法拟合

6.标量函数求根
brentq ---classic Brent (1973)
brenth ---A variation on the classic Brent（1980）
ridder ---Ridder是提出这个算法的人名
bisect ---二分法
newton ---牛顿法
fixed_point

7.多维函数求根
fsolve ---通用
broyden1 ---Broyden’s first Jacobian approximation.
broyden2 ---Broyden’s second Jacobian approximation
newton_krylov ---Krylov approximation for inverse Jacobian
anderson ---extended Anderson mixing
excitingmixing ---tuned diagonal Jacobian approximation
linearmixing ---scalar Jacobian approximation
diagbroyden ---diagonal Broyden Jacobian approximation

8.实用函数
line_search ---找到满足强Wolfe的alpha值
check_grad ---通过和前向有限差分逼近比较检查梯度函数的正确性
'''

#%% fmin_tnc
#使用truncated Newton算法中的迭代信息，最小化目标函数
import scipy.optimize as opt
'''
函数说明：
result = opt.fmin_tnc(func=ObjectiveFunction, x0=InitialValue[ndarray], fprime='目标函数的梯度', args=('目标函数额外的参数'))

结果说明：dir(opt)
x : (ndarray) The solution, that is theta.
nfeval : (int) The number of function evaluations.
rc : (int) Return code, see below
'''

result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))



#%% minimize
#使用不同最优化算法，最小化目标函数
'''
函数说明：
fmin = minimize(fun=ObjectiveFunction, x0=InitialValue[ndarray], args=('目标函数额外的参数'), 
                method='TNC', jac=True, options={'maxiter': 250})

method：最优化算法
{ 'Nelder-Mead'
'Powell'
'CG'
'BFGS'
'Newton-CG'
'L-BFGS-B'
'TNC'
'COBYLA'
'SLSQP'
'dogleg'
'trust-ncg' }

jac: Only for CG, BFGS, Newton-CG, L-BFGS-B, TNC, SLSQP, dogleg, trust-ncg.
jac = True, 返回目标函数的梯度

options is dict, options = {'maxiter':'最大迭代次数', 'disp':True[返回收敛信息]}


结果说明：
dir(fmin)    #['fun', 'jac', 'message', 'nfev', 'nit', 'status', 'success', 'x']
fmin.fun    #J (ndarray) Values of objective function
fmin.jac    #? (ndarray) Values of Jacobian
fmin.message    #'Linear search failed' (str) Description of the cause of the termination.
fmin.nfev    #223? (int) Number of evaluations of the objective functions and of its Jacobian and Hessian.
fmin.nit    #15? (int) Number of iterations performed by the optimizer.
fmin.status    #4? (int) Termination status of the optimizer.
fmin.success    #False (bool) Whether or not the optimizer exited successfully.
fmin.x    #theta (ndarray) The solution of the optimization.
'''

fmin = minimize(fun=costReg, x0=theta, args=(X, y_i, learning_rate), method='TNC', jac=gradient)

fmin = minimize(fun=backprop, x0=params, args=(input_size, hidden_size, num_labels, X, y_onehot, learning_rate), 
                method='TNC', jac=True, options={'maxiter': 250, 'disp':True})

res = opt.minimize(fun=regularized_cost,
                   x0=theta,
                   args=(X, y, l),
                   method='TNC',
                   jac=regularized_gradient,
                   options={'disp': True})

final_theta = res.x
