# -*- coding: utf-8 -*-
"""============================================================================

============================================================================"""
#%%% import modules
import xlrd, codecs, os

#%%% inputs and outputs
input_path = 'Download/'
output_path = 'Excel2Txt/'

implication2abbr = {'Online Mendelian Inheritance in Man':'MendelianInheritance',
                    'UniProtKB/Swiss-Prot':'UniProtKB_SwissProt',
                    'The University of Copenhagen DISEASES':'CopenhagenUniversity'}

#%%% define functions

#%%%
for file in os.listdir(input_path):
    print('正在处理的文件：', file)
    out_path = output_path+file.split('.')[0]+'/'
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    data = xlrd.open_workbook(input_path+file)
    sheet = data.sheets()[0]
    i = 0
    while i <= (sheet.nrows-1):
        row_values = sheet.row_values(i)
        i += 1

        if str(row_values[0]).startswith('##Genetic Tests'):
            print(' 找到对应组分：Genetic Tests')
            outfile = codecs.open(out_path+'3.2.9 GeneticTest.txt', 'w', 'utf-8')
            outfile.write('GeneticTest\tAffiliatingGenes\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#Genetic test': continue
                if row_values[0] == '': break
                tem = list(map(str, row_values[0:2]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()

        if row_values[0] == '##Genes':
            print(' 找到对应组分：Genes')
            genes_list = []
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '':break
                if type(row_values[0]) == str: continue
                genes_list.append(row_values)
            implication = []
            for gene in genes_list:
                implication.append(gene[4])
            imp_col_name = set()
            for imp in implication:
                imp = imp.split('GeneCards:')[0]
                imp = imp.split('|')
                imp = list(map(lambda x:x.split(':')[0], imp))
                for tem in imp:
                    imp_col_name.add(implication2abbr.get(tem, tem))
            imp_col_name = list(imp_col_name)
            if '' in imp_col_name: imp_col_name.remove('')

            outfile = codecs.open(out_path+'3.2.1 RelatedGenes.txt', 'w', 'utf-8')
            outfile.write('id\tSymbol\tDescription\tScore\t')
            if len(imp_col_name) == 0:
                outfile.write('GeneCards\n')
            else:
                outfile.write('\t'.join(imp_col_name)+'\tGeneCards\n')
            for gene in genes_list:
                id_num = str(int(gene[0]))
                symbol = gene[1].split(' (')[0]
                descri = gene[2]
                score = str(gene[3])
                outfile.write('\t'.join([id_num, symbol, descri, score])+'\t')
                implication = gene[4].split('GeneCards:')
                genecards = list(map(lambda x:x.strip('|'), implication[1:]))
                genecards = '|'.join(genecards)
                if genecards == '': genecards = ''
                other = implication[0].split('|')
                imp2value = {}
                for tem in other:
                    if tem == '': continue
                    tem = tem.split(':')
                    imp2value[implication2abbr.get(tem[0], tem[0])] = tem[1]
                tem = []
                for imp in imp_col_name:
                    tem.append(imp2value.get(imp, ''))
                if len(imp_col_name) == 0:
                    outfile.write(genecards+'\n')
                else:
                    outfile.write('\t'.join(tem)+'\t'+genecards+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##UniProtKB/Swiss-Prot'):
            print(' 找到对应组分：UniProtKB_Swiss-Prot')
            outfile = codecs.open(out_path+'3.2.5 UniProtKB_Swiss-Prot.txt', 'w', 'utf-8')
            outfile.write('id\tSymbol\tAA_change\tVariation_ID\tSNP_ID\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:5]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Clinvar'):
            print(' 找到对应组分：Clinvar')
            outfile = codecs.open(out_path+'3.2.2 Clinvar.txt', 'w', 'utf-8')
            outfile.write('id\tGene\tVariation\tType\tSignificance\tSNP ID\tAssembly\tLocation\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                outfile.write('\t'.join(row_values[1:8])+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Cosmic'):
            print(' 找到对应组分：Cosmic')
            outfile = codecs.open(out_path+'3.2.3 Cosmic.txt', 'w', 'utf-8')
            outfile.write('id\tCosmic_Mut ID\tGene_Symbol\tCOSMIC_Disease_Classification\tMutation_CDS\tMutation AA\tConf\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:6]))
                outfile.write('\t'.join(tem)+'\t'+str(int(row_values[6]))+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Copy number'):
            print(' 找到对应组分：CNVD')
            outfile = codecs.open(out_path+'3.2.4 CNVD.txt', 'w', 'utf-8')
            outfile.write('id\tCNVD_ID\tChromosom\tStart\tEnd\tType\tGene_Symbol\tCNVD_Disease\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(lambda x:str(x).split('.')[0], row_values[1:5]))
                outfile.write('\t'.join(tem)+'\t')
                outfile.write('\t'.join(row_values[5:8])+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Genes differentially expressed'):
            print(' 找到对应组分：LifeMap')
            outfile = codecs.open(out_path+'3.2.6 LifeMap.txt', 'w', 'utf-8')
            outfile.write('id\tGene\tDescription\tTissue\tUp_Dn\tFold_Change_log2\tP_value\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:7]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Pathways related') and \
           'GeneCards Suite' in str(row_values[0]):
            print(' 找到对应组分：Pathways')
            outfile = codecs.open(out_path+'3.2.7 Pathways.txt', 'w', 'utf-8')
            outfile.write('id\tSuper_pathways\tScore\tTop_Affiliating_Genes\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:4]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()

        if str(row_values[0]).startswith('##Cellular components'):
            print(' 找到对应组分：GO_Cellular components')
            if os.path.exists(out_path+'3.2.8 Go.txt'):
                header = False
            else:
                header = True
            outfile = codecs.open(out_path+'3.2.8 Go.txt', 'a', 'utf-8')
            if header:outfile.write('id\tName\tGO_ID\tScore\tTop_Affiliating_Genes\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:5]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()
        if str(row_values[0]).startswith('##Biological processes'):
            print(' 找到对应组分：GO_Biological processes')
            if os.path.exists(out_path+'3.2.8 Go.txt'):
                header = False
            else:
                header = True
            outfile = codecs.open(out_path+'3.2.8 Go.txt', 'a', 'utf-8')
            if header:outfile.write('id\tName\tGO_ID\tScore\tTop_Affiliating_Genes\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:5]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()
        if str(row_values[0]).startswith('##Molecular functions'):
            print(' 找到对应组分：GO_Molecular functions')
            if os.path.exists(out_path+'3.2.8 Go.txt'):
                header = False
            else:
                header = True
            outfile = codecs.open(out_path+'3.2.8 Go.txt', 'a', 'utf-8')
            if header:outfile.write('id\tName\tGO_ID\tScore\tTop_Affiliating_Genes\n')
            while True:
                row_values = sheet.row_values(i)
                i += 1
                if row_values[0] == '#id': continue
                if type(row_values[0]) == str: break
                outfile.write(str(int(row_values[0]))+'\t')
                tem = list(map(str, row_values[1:5]))
                outfile.write('\t'.join(tem)+'\n')
            outfile.close()
