# -*- coding: utf-8 -*-
"""
Created on Sat May 13 07:40:41 2023

@author: imron
"""

filename = 'add/student.txt'
with open(filename) as file:
    for line in file:
        print(line)