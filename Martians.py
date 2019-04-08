# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:58 2019

@author: Ilya Petin
"""

class Directions:
    def __init__(self, dirs, turn = "N"):
        self.directions = dirs
        self.max = len(dirs)
        self.rotate_to = turn
        
    def get_rotation_from_direction(self, turn):
        self.n = self.d
        
    def __iter__(self):
        self.n = self.directions.index(self.rotate_to)
        return self
    
    def __next__(self):
        self.n += 1
        if self.n >= self.max:
            self.n = 0         
        return self.angle()
            
    def __prev__(self):    
        self.n -= 1
        if self.n < 0: 
            self.counter_clockwise()
        return self.angle()
    
    def counter_clockwise(self):
        self.n = self.max - 1
        return self.n
    
    def clockwise(self):
        self.n = 0 
        return self.n
    
    def angle(self):
        return self.directions[self.n]  
        

class Martian():
    def __init__(self, start_post, d ):
        self.x = start_post[0]
        self.y = start_post[1]
        self.direction = iter(Directions(["N", "E", "S", "W"], d))

    def left(self):
        next(self.direction)
        
    def right(self):
        self.direction.__prev__()
    
class Martians:       
    martians = []
    
    def main(self):
        print('starting martians')
        
    def createMartian(self, x, y, d = "N"):
        self.martians.append(Martian([x, y], d))
        
    def setup(self):
        pass

if __name__ == '__main__':
    game = Martians()
    game.main()