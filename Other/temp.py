# -*- coding: utf-8 -*-
"""
Spyder Editor: LTT
This is a temporary script file.
"""

"""
#%% open操作函数1
def openNew(inputfile,outputfile):
    fh = open(inputfile)
    out = open(outputfile,'w')
    for line in fh.readlines():
        one = line.split("\t")
        one[0] = one[0].replace("chr","")
        out.write('__'.join(one)+'\n')  ##写出文件
    fh.close()
    out.close()

openNew('D:/Learn/Python/test/test.txt','D:/Learn/Python/test/out.txt')

# open操作函数2
def openNew(inputfile,outputfile):
    fh = open(inputfile)
    out = open(outputfile,'w')
    while 1:
        line1 = fh.readline()
        if line1 != "":        
            #print(line1)                  
            one = line1.strip().split("\t")
            one[0] = one[0].replace("chr","")
            out.write('__'.join(one)+'\n')
        else:
            break
    fh.close()
    #out.close()    
openNew('D:/Learn/Python/test/test.txt','D:/Learn/Python/test/out2.txt')

#%% 读取文件行数
count=len(open('D:/Learn/Python/test/out.txt').readlines())

#%% 自定义函数1
def abc(a,b,c):
    return a*100+b*10+c
print(abc(11,12,13))

#自定义函数2
def new(s):
    res=[]
    for i in range(len(s)):
        #print(i)
        res.append(s[i])
        res.append("**")
    return(res)    
print(new("ababab"))

#%% which function
def indexNew(list1,ba):
    start = 0   
    index = []    
    for i in range(len(list1)):
        res = list1.find(ba,start)
        if res == -1:
            break
        index.append(res)
        start = res+1
    return(index)   
        
list1="abababssat"
print(indexNew(list1,"ab"))

#which function2
import re   
list1="abababssat"
index = [m.start() for m in re.finditer("ab", list1)]
print(index)

#group()返回被 RE 匹配的字符串
#start()返回匹配开始的位置
#end()返回匹配结束的位置
#span()返回一个元组包含匹配 (开始,结束) 的位置
    
#print(re.findall("a",list1))
#print(list1.index("a"))
#print(list1.find("a"))

#%% re.compile()
import re
pattern=re.compile('[a-zA-Z]') #get a pattern
res=pattern.findall('siHI2hj$e')
print(res) #['s', 'i', 'H', 'I', 'h', 'j', 'e']

#%% re.findall() and re.finditer()区别
re.findall(r'[a-z]',"siiIHKH34ss") #['s', 'i', 'i', 's', 's']
[m.start() for m in re.finditer(r'[a-z]',"siiIHKH34ss")] #[0, 1, 2, 9, 10]
[m.group() for m in re.finditer(r'[a-z]',"siiIHKH34ss")] #['s', 'i', 'i', 's', 's']

#%% range
range(1,5) #[1,2,3,4]不包括5
range(1,5,2) #[1,3]隔两个输出

#%% split
list1.split("a") #同re.split("a",list1)

#%% 仅在本脚本中运行的代码行，而在该脚本被调用时不运行
if __name__ == '__main__':‘

#%% 判断以XXX开头或结尾
if filename.startwith("xxx"):
    #TRUE
if filename.endwith(".jpg"):
    #TRUE

#%% 删除
del list1
del list1[0]

#%% join
'\t'.join("ssss")

#%% 判断一个list中是否有某个元素
def getSeq(seq,dic):
    seqlist=list(seq)
    res = []
    for base in seqlist:
        if base in dic:
            res.append(dic[base])
        if base not in dic:
            res.append("N")
    return res
      
dic = {"A":"T","T":"A","G":"C","C":"G"}
seq="ATCTGTGCSGATDG"
tt=getSeq(seq,dic)
print(tt)

#%% 判断是否存在某个路径或文件
import os
os.path.exists(r'C:\1.TXT')

#%% do nothing
if filename.startwith("XX"):
    #TRUE
else:
    pass

#%% get current time from Linux
import os
os.system('date')
#or
import time
time.localtime()

#%% Python调用shell
os.system(cmd) #返回值是脚本的退出状态码
os.popen(cmd) #返回值是脚本执行过程中的输出内容
os.system('date')
os.popen('date').read()
os.popen('ls /work1/xuelab/project/ |grep liutt').read()

#%% 抛出异常
import sys
sys.exit(0) #无错误退出
sys.exit(1) #有错误退出

#%% 外部传参
import sys
sys.argv #命令行参数List，第一个元素是程序本身路径
sys.argv[0] #即test.py所在路径,不用考虑
sys.argv[1] #arg1
sys.argv[2] #arg2
sys.argv[3] #arg3
...
#调用
python test.py arg1 arg2 arg3
   
"""


    