# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:15:57 2021

@author: dvisw
"""

class animal:
    def __init__(self,color,name,food,area):
        self.color=color
        self.name=name
        self.food=food
        self.area=area
    def show(self):
        
        print(self.name+" is an animal of color "+self.color)
        print(self.name+" eats "+self.food)
        print(self.name+" lives primarily in "+self.area+" areas")

if __name__=="__main__":
    cat=animal("white", "cat","mice","urban")   
    cat.show()
    
         