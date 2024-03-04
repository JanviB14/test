# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:33:43 2024

@author: janvi
"""

from random import randint


for i in range(1,11):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print ('fizzbuzz')
    else:
        print(i)
        
        
        