# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:58 2019

@author: Ilya Petin
"""

class BaseCommand:
    def __init__(self,command_keyword, **kwargs):
        self.command_keyword = command_keyword
                
    def execute(self):
        raise Exception("must not be called directly")
        
class BaseMoveCommand(BaseCommand):
    robot = None
    
    def __init__(self,command_keyword, **kwargs):        
        super().__init__(command_keyword,kwargs)
        for key, value in kwargs.items():
            if key == "robot":
                self.robot = value

            
class Command_MoveLeft(BaseMoveCommand):    
    def __init__(self,command_keyword, **kwargs):        
        super().__init__(command_keyword,kwargs)
        
    def execute(self):
        print ("calling left command")
        next(self.robot.position)
        
class Command_MoveRight(BaseMoveCommand):    
    def __init__(self,command_keyword, **kwargs):        
        super().__init__(command_keyword,kwargs)
        
    def execute(self):
        print ("calling left command")
        self.robot.position.__prev__()
        
class Commands:
    L = "L"
    R = "R"
    F = "F"
    
    def factory(self,command):
        if(self.command_exists(command)):
            if(command == Commands.L):
                return Command_MoveLeft()
            elif(command == Commands.R):
                return Command_MoveRight()
            elif(command == Commands.F):
                print("not implemented")
        else:
            raise Exception("Command does not exist")      
    
    def get_list(self):
        return [self.L,self.R,self.F]
    
    def command_exists(self, command):
        return command in self.get_list()
    
class Directions:
    N = "N"
    S = "S"
    W = "W"
    E = "E"
    
    def get(self):
        return [self.N, self.S, self.W, self.E]
    #could have made it into an Enum too    
    def __init__(self, dirs, turn = N):
        self.directions = dirs
        self.max = len(dirs)
        self.rotate_to = turn
                
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
        
class Grid:
    def __init___(self, width, height):
        pass


class Martian:    
    def __init__(self, start_post, d ):
        self.x = start_post[0]
        self.y = start_post[1]
        self.direction = iter(Directions([Directions.N, Directions.E, 
                                          Directions.S, Directions.W], d))

    def right(self):
        self.direction.__prev__()
        
    def forward(self):
        pass        
    
class Martians:
    martians = []
    
    def main(self):
        print('starting martians')
        
    def createMartian(self, x, y, d = Directions.N):
        self.martians.append(Martian([x, y], d))
        
    def setup(self):
        pass

if __name__ == '__main__':
    game = Martians()
    game.main()