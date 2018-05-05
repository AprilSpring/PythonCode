# -*- coding: utf-8 -*-
"""
author       : Xiaojun Wang
create date  : 20151201
modified date: 20151218
verstion     : 2.0
#==============================================================================
# extract sequence based the site(start and end) and chromosome number
#==============================================================================
20151218: add -l option (default:100)
"""
#%%% import modules
import os
import getopt
import sys

#%%% define functions
def Help():
    print 'usage : python codename.py -c chromosome -s start -e end'
    print '        python codename.py -c chromosome -s start -l length'
    print '        python codename.py -c chromosome -s start'
    print '-h, --help:    print help message'
    print '-v, --version: version information'
    print '-a, --author:  author information'
    print '-c, --chr:     chromosome number (1, 2, ... X, Y, M)'
    print '-s, --start:   the start site of sequence'
    print '-e, --end:     the end site of sequence (optional)'
    print '-l, --length:  the sequence length. when -e is provided, -l is invalid'


def Version():
    print 'Version 2.0'


def Author():
    print 'Author: Xiaojun Wang'

#%%
if __name__ == '__main__':
    argv=sys.argv
    try:
        opts, args = getopt.getopt(argv[1:],'hvac:s:e:l:',
                                   [
                                   'help',
                                   'version',
                                   'author',
                                   'chr=',
                                   'start=',
                                   'end=',
                                   'length='
                                   ])
    except getopt.GetoptError, error:
        Help()
        sys.exit(2)
    for o,a in opts:
        if o in ('-h', '--help'):
            Help()
            sys.exit()
        elif o in ('-v', '--version'):
            Version()
            sys.exit()
        elif o in ('-a', '--author'):
            Author()
            sys.exit()
        elif o in ('-c', '--chr'):
            chrno = a
        elif o in ('-s', '--start'):
            start = a
            trueend = int(start)+100-1
        elif o in ('-l', '-length'):
            length = a
            trueend = int(start)+int(length)-1
        elif o in ('-e', '--end'):
            end = a
        else:
            print 'unhandled option'
            sys.exit(3)
#%% main process  #############################
    try:
        end = end
    except:
        end = trueend
    hg19Path = '/work1/xuelab/project/wangxj/data/hg19/'
    seqlist = open(hg19Path+'chr'+str(chrno)+'.fasta').readlines()
    sequence = ''.join(seqlist)
    sequence = sequence.replace('\n', '')
    print 'chr'+str(chrno)
    seqlen = int(end)-int(start)+1
    if (seqlen-len(str(start))-1)>0:
        print str(start)+' '*(seqlen-len(str(start))-1)+str(end)
    else:
        print str(start)+'  '+str(end)
    print sequence[(int(start)-1):int(end)]
    ###########################################
