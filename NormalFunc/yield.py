# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:24:29 2018

@author: User
"""

#yield 使用浅析

#method1
def fab(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       print(b)
       a, b = b, a + b 
       n = n + 1

fab(5)

#method2: 耗用内存大
def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L


#method3
class Fab(object): 
   def __init__(self, max): 
       self.max = max 
       self.n, self.a, self.b = 0, 0, 1 
 
   def __iter__(self): 
       return self 
 
   def next(self): 
       if self.n < self.max: 
           r = self.b 
           self.a, self.b = self.b, self.a + self.b 
           self.n = self.n + 1 
           return r 
       raise StopIteration()


for n in Fab(5): 
    print(n)


#method4
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

for n in fab(5): 
    print(n)


'''
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个generator，调用fab(5)不会执行fab函数，而是返回一个iterable对象

yield必须在function里面使用，不能直接用在function外面
'''
















