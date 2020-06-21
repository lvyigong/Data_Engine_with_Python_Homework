# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:35:01 2020

@author: alienware
"""

'''
Mission 3: 汽车质量数据统计
1. 数据导入
2. 数据预处理：拆分问题类型——多个字段
3. 数据统计：投诉总数并排序；不同问题类型的总数并排序；
'''

print('----Mission 3---')

import pandas as pd
from pandas import DataFrame

print('原始数据导入：')
CarData=DataFrame(pd.read_csv('car_complain.csv'))
print(CarData)

print('数据预处理：')
CarData['brand'].replace('一汽-大众','一汽大众',inplace=True)
problem =CarData.problem.str.get_dummies(',')
tags=problem.columns
Carname=CarData.loc[:,['brand','car_model']]
CarData=pd.concat([Carname,problem],axis=1)
print(CarData)
CarData.to_excel('CarData.xlsx')

print('数据统计：')
#按品牌统计投诉总数并排序
brand_count=CarData.groupby(['brand'])[tags].agg(['sum'])
brand_count['品牌count']=brand_count.sum(axis=1)
brand_count=brand_count.sort_values('品牌count',ascending=False)
brand_count=brand_count.drop(tags,1)
print(brand_count)
#按车型统计投诉总数并排序
model_count=CarData.groupby(['car_model'])[tags].agg(['sum'])
model_count['车型count']=model_count.sum(axis=1)
model_count=model_count.sort_values('车型count',ascending=False)
model_count=model_count.drop(tags,1)
print(model_count)
