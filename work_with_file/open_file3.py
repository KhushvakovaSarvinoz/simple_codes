# -*- coding: utf-8 -*-
"""
Created on Sat May 13 07:53:58 2023

@author: imron
"""

with open('add/student.txt') as file:
    student=file.readlines()
    print(student)
    student= [student.rstrip() for student in student]
    print(student)