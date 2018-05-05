# -*- coding: utf-8 -*-
"""============================================================================

============================================================================"""
#%%% import modules
import codecs, os
from collections import OrderedDict, defaultdict

#%%% inputs and outputs
input_path = 'Excel2Txt/'
genes_file = '/3.2.1 RelatedGenes.txt'
cosmic_file = '/3.2.3 Cosmic.txt'
cnvd_file = '/3.2.4 CNVD.txt'
life_file = '/3.2.6 LifeMap.txt'
path_file = '/3.2.7 Pathways.txt'
goid_file = '/3.2.8 Go.txt'
test_file = '/3.2.9 GeneticTest.txt'
merge_file = '/3.2.10 Merge.txt'

#%%% define functions

#%%% 检查基因的表头可能存在的情况
gene_header = set()
for dirs in os.listdir(input_path):
    if not os.path.exists(input_path+dirs+genes_file): continue
    print(dirs)
    for line in codecs.open(input_path+dirs+genes_file, 'r', 'utf-8'):
        break
    linelist = line.strip('\r\n').split('\t')
    gene_header.update(linelist[4:])
gene_header = list(gene_header)

#%% 每个癌症文件夹中分别合并文件产生 3.2.10 Merge.txt
for dirs in os.listdir(input_path):
    if not os.path.exists(input_path+dirs+genes_file): continue
    print(dirs)

    outfile = codecs.open(input_path+dirs+merge_file, 'w', 'utf-8')

    gene2line = OrderedDict()
    header = True
    for line in codecs.open(input_path+dirs+genes_file, 'r', 'utf-8'):
        if header:
            header_list = line.strip('\r\n').split('\t')
            header_num = [] # 1.用来在现有文件标题后添加新标题; 2.长度决定需要补齐的空列
            for head in gene_header:
                if head in header_list: continue
                header_num.append(head)
            header_list.extend(header_num)
            outfile.write('\t'.join(header_list)+'\t')
            outfile.write('Cosmic_Mut ID\tCNVD_Type\tUp_Dn\tSuper_pathways\tGO_ID\tGeneticTest\n')
            header = False
            continue
        linelist = line.strip('\r\n').split('\t')
        gene2line[linelist[1]] = line.strip('\r\n')

    gene2cosmic = defaultdict(set)
    if os.path.exists(input_path+dirs+cosmic_file):
        header = True
        for line in codecs.open(input_path+dirs+cosmic_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            if not linelist[2]: continue
            gene2cosmic[linelist[2]].add(linelist[1])

    gene2cnvd = defaultdict(set)
    if os.path.exists(input_path+dirs+cnvd_file):
        header = True
        for line in codecs.open(input_path+dirs+cnvd_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            if not linelist[6]: continue
            gene2cnvd[linelist[6]].add(linelist[5])

    gene2life = defaultdict(set)
    if os.path.exists(input_path+dirs+life_file):
        header = True
        for line in codecs.open(input_path+dirs+life_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            if not linelist[1]: continue
            gene2life[linelist[1]].add(linelist[4])

    gene2path = defaultdict(set)
    if os.path.exists(input_path+dirs+path_file):
        header = True
        for line in codecs.open(input_path+dirs+path_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            genes = linelist[3].split('|')
            for gene in genes:
                if not gene: continue
                gene2path[gene].add(linelist[1])

    gene2goid = defaultdict(set)
    if os.path.exists(input_path+dirs+goid_file):
        header = True
        for line in codecs.open(input_path+dirs+goid_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            genes = linelist[4].split('|')
            for gene in genes:
                if not gene: continue
                gene2goid[gene].add(linelist[2])

    gene2test = defaultdict(set)
    if os.path.exists(input_path+dirs+test_file):
        header = True
        for line in codecs.open(input_path+dirs+test_file, 'r', 'utf-8'):
            if header:
                header = False
                continue
            linelist = line.strip('\r\n').split('\t')
            genes = linelist[1].split('|')
            for gene in genes:
                if not gene: continue
                gene2test[gene].add(linelist[0])

    #Cosmic_Mut ID\tCNVD_Type\tUp_Dn\tSuper_pathways\tGO_ID\tGeneticTest
    for gene in gene2line:
        outfile.write(gene2line[gene]+'\t'*len(header_num))
        outfile.write('\t'+'\t'.join(['|'.join(gene2cosmic.get(gene, set())),
                                      '|'.join(gene2cnvd.get(gene, set())),
                                      '|'.join(gene2life.get(gene, set())),
                                      '|'.join(gene2path.get(gene, set())),
                                      '|'.join(gene2goid.get(gene, set())),
                                      '|'.join(gene2test.get(gene, set()))
                                      ])+'\n')
    outfile.close()

#%% 合并所有的 3.2.10 Merge.txt 文件到一个文件中。
gene_cancer2line = {}
static_header = ['Description', 'Score', 'CopenhagenUniversity', 'GeneCards',
                 'Orphanet', 'Novoseek', 'ClinVar', 'UniProtKB_SwissProt',
                 'MendelianInheritance', 'Cosmic_Mut ID', 'CNVD_Type', 'Up_Dn',
                 'Super_pathways', 'GO_ID', 'GeneticTest']

for dirs in os.listdir(input_path):
    if not os.path.exists(input_path+dirs+merge_file): continue
    print(dirs)

    header = True
    for line in codecs.open(input_path+dirs+merge_file, 'r', encoding='utf-8'):
        if header:
            header = False
            header_list = line.strip('\r\n').split('\t')
            continue
        linelist = line.strip('\r\n').split('\t')
        newline = []
        for tem in static_header:
            newline.append(linelist[header_list.index(tem)])
        newline = '\t'.join(newline)+'\n'
        gene_cancer2line.setdefault(linelist[1], [])
        gene_cancer2line[linelist[1]].append(dirs+'\t'+newline)

gene2num = sorted(gene_cancer2line.items(), key=lambda x:len(x[1]), reverse=True)
outfile = codecs.open('MergeAll.txt', 'w', 'utf-8')
outfile.write('Symbol\tCancerName\t'+'\t'.join(static_header)+'\n')
for gene in gene2num:
    gene = gene[0]
    for tem in gene_cancer2line[gene]:
        outfile.write(gene+'\t'+tem)
outfile.close()
