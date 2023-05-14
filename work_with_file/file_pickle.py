# -*- coding: utf-8 -*-
"""
Created on Sun May 14 06:41:19 2023

@author: imron
"""
import pickle
python_dictionary = {'int': 'butun son', 'float':'kasr son', 'string':'matn'}
python_dictionary1 = {'if':'agar', 'else':'yoki', 'for':'uchun'}

with open("PI.txt", 'wb') as file:
    pickle.dump(python_dictionary,file)
    pickle.dump(python_dictionary1,file)
    