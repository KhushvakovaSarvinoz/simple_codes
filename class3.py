# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:38:58 2023

@author: imron
"""
class Avto_salon:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.avtos = []
        self.avto_number = 0
        
    def add_avto(self, avto):
        self.avtos.append(avto)
        self.avto_number +=1
    
    def get_name(self):
        return self.name
    def get_adress(self):
        return self.adress

    def get_avtos(self):
        return [x.get_info() for x in self.avtos]  
    
    
salon1= Avto_salon("Flora", "Naperville")


print(salon1.get_name())
print(salon1.get_adress())


class Avto:
    def __init__(self,color,brand,model,price,data):
        self.color = color
        self.brand = brand
        self.price = price
        self.data = data
        self.model = model
        self.km = 0
        
    def get_color(self):
        return self.color
    
    def get_brand(self):
        return self.brand
    
    def get_price(self):
        return self.price
    
    def get_data(self):
        return self.data
    
    def set_km(self,km):
        self.km = km
        
    def get_km(self):
        return self.km
        
    def get_info(self):
        return f"{self.color} {self.model}, brand: {self.brand}, price: {self.price} data {self.data} kilometr: {self.km}"
   
    
avto1 = Avto("red", "toyota", "Corolla Cross XLE", 13000,2017)
avto2 = Avto("black", "BMW","X7", 17000,2020)
avto3 = Avto("white", "Tesla","Model X", 30000,2022)

print(avto1.get_color())
print(avto3.get_price())
print(avto2.get_info())
avto2.set_km(23) 
print(avto2.get_km())

salon1.add_avto(avto1)
salon1.add_avto(avto2)
salon1.add_avto(avto3)

print(avto1.__dict__)
