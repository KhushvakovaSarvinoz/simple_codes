# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:38:58 2023

@author: imron
"""
class Human:
    def __init__(self, name, surname, pasport, byear):
        self.name= name
        self.surname= surname
        self.pasport= pasport
        self.byear= byear
        
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_pasport(self):
        return self.pasport
    
    def get_byear(self):
        return self.byear
    def get_info(self):
        info= f"Full name is {self.name} {self.surname} pasport: {self.pasport} birth year is {self.byear}"
        return info
    
    
person= Human("Sarvinoz","Xushvaqova", "AB0014701", 1994)

class Student(Human):
    def __init__(self,name,surname,pasport,byear, ID):
        super().__init__(name,surname,pasport,byear)
        self.ID= ID
        self.course= 1
        self.subjects= []
        
    def get_ID(self):
        return self.ID
    
    def get_course(self):
        return self.course
    
    def set_course(self, course):
        return self.course
    
    def get_info(self):
        info=f"Student {self.name} {self.surname} ID: {self.ID} course: {self.course}"
        return info
    
student= Student("Imron","Akmaljonov","AA203434", 2000, 374494923)

        
        