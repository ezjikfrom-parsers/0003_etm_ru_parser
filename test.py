# -*- coding: utf-8 -*-
'''
Created on 27.08.2020

@author: Sergey
'''
import pickle

with open('products.pickle', 'rb') as f:
        data_new = pickle.load(f);
        
for i in data_new:
    print(i)
    
print(data_new)