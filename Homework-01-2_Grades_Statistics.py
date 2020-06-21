# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:45:31 2020

@author: alienware
"""

'''
Mission 2: 班级成绩统计
1. 数据统计
2. 总成绩排序
'''
print('----Mission 2---')

from pandas import DataFrame

grade = DataFrame({'Name':['吕布','赵云','典韦','关羽','马超'],
                   'Chinese':[76,98,57,83,90],
                   'Math':[83,94,77,87,98],
                   'German':[44,39,86,71,55]})
print('本次成绩：')
print(grade)
print('成绩统计：')
print(grade.describe())
def sum_grade(x):
    x['总成绩']=x['Chinese']+x['Math']+x['German']
    return x
grade=sum_grade(grade)
print(grade.sort_values('总成绩',ascending=False))
