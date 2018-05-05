# -*- coding: utf-8 -*-
################################################
#将字符转换成数值字符############################
###############################################
def change_chr_value(inpath,outpath):
    inputfile = open(inpath)
    outfile = open(outpath,'w')
    i = 1
    while 1:
        raw = inputfile.readline().strip()   ##去除读入文件末尾的‘\n’
        chrk = raw.split('\t')   ##按TAB键分割
        if len(raw) == 0:
            break
        i=i+1
        print(i)
        chrk[1] = chrk[1].zfill(9)   #填充，不够9位，以0填满
        chrk0 = chrk[0].upper().replace('CHR','')   #转换成大写，之后替换
        if len(chrk0) == 1:
            if chrk0 == 'M':
                chrk[0] = '25'
            elif chrk0 == 'Y':
                chrk[0] = '24'
            elif chrk0 == 'X':
                chrk0 = '23'
            else:
                chrk[0] = chrk0.zfill(2)
        if len(chrk0) == 2:
            if chrk0 == 'MT':
                chrk[0] = '26'
            else:
                chrk[0] = chrk0
        #print('\t'.join(chrk)+'\n')
        outfile.write('\t'.join(chrk)+'\n')  ##写出文件
    
    inputfile.close()
    outfile.close()
    
change_chr_value(inpath='dbsnp_138.b37',outpath='changechrvalue.txt') 

##由数值字符转换成字符
def change_value_chr(inpath,outpath):
    input2 = open(inpath)
    outfile = open(outpath,'w')
    while 1:
        raw2 = input2.readline().strip()
        if len(raw2) == 0:
            break
        chrg = raw2.split('\t')       
        chrg[1] = str(int(chrg[1]))
        chrg0 = int(chrg[0])
        if chrg0 == 23:
            chrg[0] ='chr'+'X'
        if chrg0 == 24:
            chrg[0] = 'chr' + 'Y'
        if chrg0 == 25:
            chrg[0] = 'chr' + 'M'
        if chrg0 == 26:
            chrg[0] = 'chr'+'MT'
        if chrg0 < 23:
            chrg[0] = 'chr'+ str(chrg0)
        #print('\t'.join(chrg)+'\n')
        outfile.write('\t'.join(chrg)+'\n')
        
    outfile.close()
    input2.close()

change_value_chr(inpath='changechrvalue.txt',outpath='changevaluechr.txt')  
    
   