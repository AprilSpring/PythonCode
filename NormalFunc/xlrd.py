# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:17:32 2018

@author: User
"""
#%% XLSX File

import xlrd

input_file_name = 'D:\temp\input.xlsx' #including path and file

#打开excel文件
workbook = xlrd.open_workbook(input_file_name)

#获取sheet
sheet = workbook.sheet_by_name(sheetname='company') #按名字
sheet = workbook.sheets()[0] #获取第一个sheet表单

#获取文件的行列数
rows = sheet.nrows
cols = sheet.ncols

#获取单元格元素
for rownum in range(0,rows):
    for colnum in range(0,cols):
        celldata = sheet.cell(rownum,colnum).value
        #...



