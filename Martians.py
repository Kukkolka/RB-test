# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:58 2019

@author: Ilya Petin
"""

class BaseCommand(object):
    def __init__(self,command_keyword, **kwargs):
        self.command_keyword = command_keyword
                
    def execute(self):
        raise Exception("must not be called directly")
        
class BaseMoveCommand(BaseCommand):
    robot = None
    
    def __init__(self,command_keyword, **kwargs):        
        super().__init__(command_keyword,**kwargs)
        for key, value in kwargs.items():
            if key == "robot":
                self.robot = value

            
class Command_MoveLeft(BaseMoveCommand):    
    def __init__(self, **kwargs):        
        super().__init__("L", **kwargs)
        
    def execute(self):
        self.robot.direction.right()
        
class Command_MoveRight(BaseMoveCommand):    
    def __init__(self, **kwargs):        
        super().__init__("R", **kwargs)
        
    def execute(self):
        self.robot.direction.left()
    
 
class Commands:
    L = "L"
    R = "R"
    F = "F"
    
    def __init__(self):
        pass
    
    def factory(self,command,**kwargs):
        if(self.command_exists(command)):
            if(command == self.L):
                return Command_MoveLeft(**kwargs)
            elif(command == self.R):
                return Command_MoveRight(**kwargs)
            elif(command == self.F):
                return Command_MoveForward(**kwargs)
        else:
            raise Exception("Command does not exist")      
    
    def get_list(self):
        return [self.L,self.R,self.F]
    
    def command_exists(self, command):
        return command in self.get_list()
    
class Directions(object):
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
        self.n = self.directions.index(self.rotate_to)
                
    def right(self):
        self.n += 1
        if self.n >= self.max:
            self.n = 0         
        return self.facing()
            
    def left(self):   
        self.n -= 1
        if self.n < 0: 
            self.counter_clockwise()
        return self.facing()
    
    def counter_clockwise(self):
        self.n = self.max - 1
        return self.n
    
    def clockwise(self):
        self.n = 0 
        return self.n
    
    def facing(self):
        return self.directions[self.n]  
    
class Command_MoveForward(BaseMoveCommand):    
    def __init__(self, **kwargs):        
        super().__init__("F", **kwargs)
        
    def execute(self):
        
        print("moving forward",self.robot.direction.facing())
        if self.robot.direction.facing() == Directions.N:
            self.robot.y += 1
        elif self.robot.direction.facing() == Directions.S:
            self.robot.y -= 1  
        elif self.robot.direction.facing() == Directions.E:
            self.robot.x += 1  
        elif self.robot.direction.facing() == Directions.W:
            self.robot.x -= 1       
            
class Grid:
    def create_new(self,size):
        self.size = size
        self.grid = [ [0] * self.size for _ in range(self.size)]
        
    def __str__(self):
        print(str(self.grid))


class Martian(object):    
    
    def __init__(self, start_post, d ):
        self.known_commands = []
        self.x = start_post[0]
        self.y = start_post[1]
        self.direction = Directions([Directions.N, Directions.E, 
                                          Directions.S, Directions.W], d)
        self.addCommand(Command_MoveForward(robot = self))
        self.addCommand(Command_MoveLeft(robot = self))
        self.addCommand(Command_MoveRight(robot = self))
        
    def addCommand(self,cmd):
        if cmd is not None:
            self.known_commands.append(cmd)
        
    def execute_command(self,cmd):
        for learned in self.known_commands:
            if cmd == learned.command_keyword:
                print("moving",cmd)
                learned.execute()

    def facing(self):
        return self.direction.facing()
    
class Martians(object):
    
    def __init__(self):
        self.martians = []
    
    def main(self):
        print('starting martians')        
        
    def createMartian(self, x, y, d = Directions.N):
        self.martians.append(Martian([x, y], d))
        
    def setup(self):
        pass

if __name__ == '__main__':
    game = Martians()
    game.main()