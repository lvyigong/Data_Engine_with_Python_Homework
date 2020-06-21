# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:29:17 2020

@author: wolverine
"""
'''
Mission 1: 求和：2+4+6+8+...+100
'''
print('----Mission 1---')

import numpy as np

x1=np.arange(2,100,2)
print("2+4+6+8+...+100="+ str(x1.sum()))