#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:27:42 2018

@author: tinghai
"""

## matplotlib

import matplotlib as plt

data[:10].plot(kind='barh', rot=0)
count_subset.plot(kind='barh', stacked=True)
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")'
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male') 
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

table.plot(style={'M': 'k-', 'F': 'k--'})


#mac终端画图，需加下面语句显示图形
plt.pyplot.show()


