# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:35:44 2021

@author: dvisw
"""

from cat import animal
class dog(animal):
    def __init__(self,color, name,food,area):
        animal.__init__(self, color, name,food,area)
    def show(self):
        animal.show(self)
if __name__=="__main__":
   german_shepard=dog("brown","german shepard","meat","urban")  
   german_shepard.show() 
   print(german_shepard.__dict__)  
   #print(german_shepard.__bases__)  
   #
   print(german_shepard.__name__)  
   