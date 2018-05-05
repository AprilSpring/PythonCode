# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:01:04 2018

@author: User
"""
#相关指标计算


#%% 绘制ROC曲线
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_true, pred, pos_label=2)


#%% 计算precision，recall和f1-score
from sklearn.metrics import precision_score, recall_score, f1_score  
 
#数据是list类型 
y_true = [0, 1, 1, 0, 1, 0]  
y_pred = [1, 1, 1, 0, 0, 1]  
  
p = precision_score(y_true, y_pred, average='binary')  
r = recall_score(y_true, y_pred, average='binary')  
f1score = f1_score(y_true, y_pred, average='binary')  


#数据是ndarray类型
import numpy as np
y_true = np.array([[0, 1, 1],   
                   [0, 1, 0]])  
y_pred = np.array([[1, 1, 1],   
                   [0, 0, 1]])  
  
y_true = np.reshape(y_true, [-1])  
y_pred = np.reshape(y_pred, [-1])  
  
p = precision_score(y_true, y_pred, average='binary')  
r = recall_score(y_true, y_pred, average='binary')  
f1score = f1_score(y_true, y_pred, average='binary') 


#%% 计算均方差
from sklearn.metrics import mean_squared_error
from math import sqrt
err = sqrt(mean_squared_error(y_true, y_pred))


#%% metircs包括的函数
from sklearn import metrics
dir(metrics)
'''
 'accuracy_score',
 'auc',
 'average_precision_score',
 'cluster',
 'coverage_error',
 'euclidean_distances',
 'explained_variance_score',
 'f1_score',
 'jaccard_similarity_score',
 'label_ranking_average_precision_score',
 'label_ranking_loss',
 'make_scorer',
 'matthews_corrcoef',
 'mean_absolute_error',
 'mean_squared_error',
 'mean_squared_log_error',
 'median_absolute_error',
 'mutual_info_score',
 'normalized_mutual_info_score',
 'pairwise',
 'pairwise_distances',
 'pairwise_distances_argmin',
 'pairwise_distances_argmin_min',
 'precision_recall_curve',
 'precision_recall_fscore_support',
 'precision_score',
 'ranking',
 'recall_score',
 'regression',
 'roc_auc_score',
 'roc_curve'
'''










