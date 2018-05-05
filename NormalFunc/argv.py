# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:34:37 2018

@author: User
"""

import sys  

a = sys.argv[1]
b = sys.argv[2]
c = a + b
print(c)

  
def main(argv):    
    print(sys.argv[0])         #脚本名字  
    #print(sys.argv[1])         ＃脚本第一个参数  
    #print(sys.argv[1:])  
  
    #print(sys.argv)            ＃脚本的所有参数  
    #print(len(sys.argv))       ＃脚本的参数个数  
    print('Succeed!')
    return 0  


if __name__ == '__main__':  
    sys.exit(main(sys.argv[1:]))  #sys.exit(0)正常退出， sys.exit(1)非正常退出 
    
