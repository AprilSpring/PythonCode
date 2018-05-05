# -*- coding: utf-8 -*-
"""
Created on Wed 2016-11-17

@author: Liutt
"""

#!/usr/bin/python
#coding:utf-8

#Function
def get_page_address(url,outputfile):
    out = open(outputfile,'a')
    out.write('Name\tAddress\tPhone\tFax\tWebsite\tProduct\n')
    html = urllib.request.urlopen(url).read().decode("utf-8")
    print("正在请求网页......")
    find_page_string=re.compile(r'<a href='+'"http://www.medicaldevices-business-review.com/companies/'+'\\w*')
    page_string=find_page_string.findall(html)
    #循环每个子网页
    for i in range(0,len(page_string)):
        print(i)
        t = re.sub(r'<a href="', '', page_string[i])+'#'
        temp = re.sub(r'http://www.medicaldevices-business-review.com/companies/','',t)
        company_name = re.sub(r'#','',temp)
        html3 = urllib.request.urlopen(t).readlines()
        for j in range(0,len(html3)-1):
            line = str(html3[j].strip()).replace('b\'','').replace('\'','')
            if line.startswith('<strong>'):
                mark1 = j
            if line.startswith('<div class="company_tab_list">'):
                mark2 = j
            if line.startswith('<h3>Products:</h3><ul>'):
                mark3 = j
        find_address = html3[mark1+1:mark2-1]
        find_address = str(find_address).replace(' ','').replace('[','').replace('b\'','').replace('<br/>\\r\\n\'','').replace(']','')
        find_phone = html3[mark2+1]
        find_phone = str(find_phone).replace(' ','').replace('b\'','').replace('<br/>\\r\\n\'','')
        find_fax = html3[mark2+2]
        find_fax = str(find_fax).replace(' ','').replace('b\'','').replace('<br/>\\r\\n\'','')
        find_www = html3[mark2+3]
        find_www = str(find_www).replace(' ','').replace('b\'','').replace('\\r\\n\'','')
        file_product = html3[mark3:]
        for j2 in range(0,len(file_product)-1):
            line = str(file_product[j2].strip()).replace('b\'','').replace('\'','')
            if line.startswith('</ul>'):
                mark4 = j2
                break
        find_product = file_product[2:mark4-1]
        find_product = str(find_product).replace('[','').replace('b\'','').replace('<li>','').replace('</li>','').replace(',','').replace(']','').replace(':\\n\'',':').replace('\\n\'',';')
        print(find_product)
        out.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (company_name,find_address,find_phone,find_fax,find_www,find_product))
    out.close()


# script
import urllib
from urllib.request import urlopen
import re
get_page_address(url='http://invitrodiagnostics.medicaldevices-business-review.com/companies',outputfile='D:/Work/Source/extractFromNet/extracOut_1.txt')
get_page_address(url='http://invitrodiagnostics.medicaldevices-business-review.com/companies/page/2',outputfile='D:/Work/Source/extractFromNet/extracOut_2.txt')



url = 'http://invitrodiagnostics.medicaldevices-business-review.com/companies'
url_page2 = 'http://invitrodiagnostics.medicaldevices-business-review.com/companies/page/2'
url_sub = 'http://www.medicaldevices-business-review.com/companies/seracare_life_sciences_inc#'






