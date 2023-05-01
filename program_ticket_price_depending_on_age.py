# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:46:27 2023

@author: imron
"""

age = int(input("Please, enter your age:\n"))
if age<5 or age>60:
    print("Enterance ticket to the museum is free for you.")
    
elif age<18:
    print("The price of enterance ticket to the museum is 10$.")
    
elif age>18:
    print("The price of enterance ticket to the museum is 20$.")