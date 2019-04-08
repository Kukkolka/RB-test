# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:58 2019

@author: Ilya Petin
"""

class Directions:
    def __init__(self, dirs):
        self.directions = dirs
        self.max = len(dirs)
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        self.n += 1
        if self.n >= self.max:
            self.n = 0         
        return self.pos()
            
    def __prev__(self):    
        self.n -= 1
        if self.n < 0: 
            self.counter_clockwise()
        return self.pos()
    
    def counter_clockwise(self):
        self.n = self.max - 1
        return self.n
    
    def clockwise(self):
        self.n = 0 
        return self.n
    
    def pos(self):
        return self.directions[self.n]  
        

    
class Martians:       
    
    def main(self):
        print('starting martians')
        
    def setup(self):
        self.directions = iter(Directions(["N", "S", "E", "W"]))

if __name__ == '__main__':
    game = Martians()
    game.main()