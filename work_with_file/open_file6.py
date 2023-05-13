# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:22:40 2023

@author: imron
"""

import pickle

student1={'name':'Dilbar', 'surname':'davronova', 'byear':1994}
student2={'name':'Durdona', 'surname':'Karimova', 'byear':1992} 
with open ('new_file.txt', 'wb') as file:
    pickle.dump(student1,file)
    pickle.dump(student2,file)