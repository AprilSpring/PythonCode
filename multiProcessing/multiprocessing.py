import math
import pandas as pd
from multiprocessing import Pool


# 1）按照进程数，对原始数据进行分片处理
def data_process(file_path, processor_num, processor_index):
    file = pd.read_csv(file_path)
    size = math.ceil(file.shape[0] / processor_num)
    start = size * processor_index #分片索引
    end = (processor_index + 1) * size if (processor_index + 1) * size < file.shape[0] else file.shape[0]
    temp_file = file.iloc[start:end]
    return temp_file.shape[0] # or do something else


# 2）开启多进程
def main():
    processor_num = 8
    file_path = './data/test.csv'
    p = Pool(processor_num)
    for i in range(processor_num):
        p.apply_async(data_process, args=(file_path, processor_num, i,)) #非阻塞异步
        print(str(i) + ' processor started !')
    p.close()
    p.join()


if __name__=='__main__':
    main()