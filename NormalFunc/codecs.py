# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:13:08 2018

@author: User
"""

#%% codecs 读入文件

#打开文件
#file = open(input_file_name,'rb')

#相比较于open(), codecs.open()在读入文件时会避免一些编码问题，建议使用
import codecs

input_file_name = 'D:\temp\input.txt' 
out_file_name = 'D:\temp\out.txt'

#读入文件
inputfile = codecs.open(input_file_name, encoding='utf-8', errors='ignore')

#写出文件
outfile = codecs.open(out_file_name, 'w', encoding='utf-8')

#写入具体内容
outfile.write('\t'.join(['gene_dict', 'change', 'sample', 'detect', 'marker'])+'\n') #使用\t进行连接

#关闭文件
outfile.close()


