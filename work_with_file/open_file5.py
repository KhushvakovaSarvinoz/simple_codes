# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:08:32 2023

@author: imron
"""

filename = "new_file.txt"
name= "Kadirov Akmal"
byear= 1986
with open(filename,'w') as file:  
    file.write(name +'\n')
    file.write(str(byear +'\n'))
    
with open(filename,'a') as file:
    file.write("Olim Sattorov")
    file.write(1988)
    