# -*- coding: UTF-8 -*-

#%%数据结构
##字符串
##加号（+）是字符串连接运算符，星号（*）是重复操作
str='Hello World!'
print(str) # 输出完整字符串
print(str[0]) # 输出字符串中的第一个字符
print(str[2:5]) # 输出字符串中第三个至第五个之间的字符串
print(str[2:]) # 输出从第三个字符开始的字符串
print(str * 2) # 输出字符串两次
print(str + "TEST")# 输出连接的字符串

##列表
##加号（+）是列表连接运算符，星号（*）是重复操作
##列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，
##从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list) # 输出完整列表
print(list[0]) # 输出列表的第一个元素
print(list[1:3]) # 输出第二个至第三个的元素 
print(list[2:]) # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2) # 输出列表两次
print(list + tinylist) # 打印组合的列表

##元组
##元组是不允许更新的。而列表是允许更新
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple) # 输出完整元组
print(tuple[0]) # 输出元组的第一个元素
print(tuple[1:3])# 输出第二个至第三个的元素 
print(tuple[2:])# 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2) # 输出元组两次
print(tuple + tinytuple) # 打印组合的元组

##元字典
##字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one']) # 输出键为'one' 的值
print(dict[2])# 输出键为 2 的值
print(tinydict)# 输出完整的字典
print(tinydict.keys()) # 输出所有键
print(tinydict.values())# 输出所有值

#%%条件语句
# 例1：if 基本用法
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print('welcome boss')    # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称

# 例2：elif用法
num = 5     
if num == 3:            # 判断num的值
    print('boss')        
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')     # 条件均不成立时输出
    
    
# 例3：if语句多个条件
num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print('hello')

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print('hello')
else:
	print('undefine')

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print('hello')
else:
    print('undefine')
	# 输出结果   
    
#%%循环语句
count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1    
    
# continue 和 break 用法
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break       
##在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
##else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
##while … else 也是一样。    
count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")  
    
for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print('当前字母 :', fruit)    
 
##函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数   
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])    
    
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')    
    
    
    
#%% 其他常用函数
celldata = str(celldata)
strnew = celldata.replace('miR', 'MIR') #将miR替换成MIR 
strnew = celldata.split('|')
celldata.startswith('MIR') #检查字符串是否是以指定子字符串开头,返回True or False
celldata.strip('\n') #移除字符串头尾指定的字符(默认为空格)

classmates = ['Michael', 'Bob', 'Tracy'] 
classmates.append('Adam') #For list,末尾添加,没有add()方法  
s={1,2,3}
s.add(8) #For set对象，末尾添加，没有append()方法
'strssss'.count('s',2) #从索引为2开始记录匹配字符串的数目

data.insert(0, 'Ones', 1) #在第1列的位置，插入列名为Ones、值为1的列

zip() #对应向量中各取一个元素
predictions = [0,1,1,1,0,0,1,0,1,0,0,1]
y = [1,1,1,0,1,0,0,0,1,1,0,1]
a = zip(predictions,y)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]   
[m,n]=zip(*zip(predictions,y))
   
map()
list(map(lambda x: x**2, [1,3,5,7])) #对每个元素运算function中内容 
accuracy = (sum(map(int, correct)) / len(correct)) #%与/的区别？

#*args和**args适用于函数的参数不确定的时候
#*args可以看做是多个变量组成的list，**args可以看做是个字典
def prepare_poly_data(*args, power):
    return [x for x in args]

#print()
print('test cost(l={}) = {}'.format(l, J))
print('test cost(l = %s) = %s' % (l, J)) #同上















