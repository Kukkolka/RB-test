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
    def __init__(self,command_keyword, **kwargs):        
        super().__init__(command_keyword,**kwargs)
        for key, value in kwargs.items():
            if key == "robot":
                self.robot = value
            
class Command_MoveLeft(BaseMoveCommand):    
    def __init__(self, **kwargs):        
        super().__init__("L", **kwargs)
        
    def execute(self):
        self.robot.direction.left()
        
class Command_MoveRight(BaseMoveCommand):    
    def __init__(self, **kwargs):        
        super().__init__("R", **kwargs)
        
    def execute(self):
        self.robot.direction.right()
    
 
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
        return self.directions
    
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
        prev_pos_x, prev_pos_y = self.robot.temp_pos[0], self.robot.temp_pos[1]
        new_pos_x, new_pos_y = self.robot.temp_pos[0], self.robot.temp_pos[1]
        if self.robot.direction.facing() == Directions.N:
            new_pos_y = prev_pos_y+1
        elif self.robot.direction.facing() == Directions.S:
            new_pos_y = prev_pos_y-1  
        elif self.robot.direction.facing() == Directions.E:
            new_pos_x = prev_pos_x+1  
        elif self.robot.direction.facing() == Directions.W:
            new_pos_x = prev_pos_x-1
        self.robot.move_to(new_pos_x,new_pos_y)
            
class Grid(object):
    grid = None
    
    def create_new(self,w,h):
        self.width = w 
        self.height = h 
        self.grid = [ [0] * (h+1) for _ in range((1+w))]
        
    def __str__(self):
        print(str(self.grid))
        
    def mark_x(self,x,y,index):
        self.grid[x][y]= index
        print(self.grid)
        
    def in_bounds(self,x,y):
        return y >= 0 and y <= self.height and x >= 0 and x <= self.width

class Martian(object):    
    
    def __init__(self, start_post, d, game):
        self.is_lost = False
        self.temp_pos = start_post
        self.game = game
        self.known_commands = []
        self.x = 0#start_post[0]
        self.y = 0#start_post[1]
        self.direction = Directions([Directions.N, 
                                     Directions.E, 
                                     Directions.S, 
                                     Directions.W], d)
        self.addCommand(Command_MoveForward(robot = self))
        self.addCommand(Command_MoveLeft(robot = self))
        self.addCommand(Command_MoveRight(robot = self))
        self.index = len(self.game.martians)+1
    
    def addCommand(self,cmd):
        if cmd is not None:
            self.known_commands.append(cmd)
        
    def execute_command(self,cmd):
        for learned in self.known_commands:
            if cmd == learned.command_keyword:
                learned.execute()
                
    def move_to(self,x, y):
        #    self.is_lost = not self.game.on_mars(x,y)
         #   if self.is_lost is not True:
        prev_pos = self.temp_pos
        self.temp_pos = [x, y]
               
        if(self.game.on_mars(x,y)):
            if(self.game.grid.grid[x][y]== 0 or self.game.grid.grid[x][y]==self.index):
                self.x = x
                self.y = y
            elif(self.game.grid.grid[x][y]!=self.index): 
                self.temp_pos = prev_pos
        self.finished_movement()
          #  else:
           #     self.game.mark_lost(self.x,self.y)
        
    def finished_movement(self):
        if not self.is_lost:
            self.is_lost = not self.game.on_mars(self.temp_pos[0],self.temp_pos[1])
        if self.is_lost:
            self.game.mark_lost(self.x,self.y,self.index)
            
    def facing(self):
        return self.direction.facing()
    
    def lost(self):
        if self.is_lost:
            return 'LOST'
        return ''
    
class Martians(object):
    
    def __init__(self):
        self.martians = []
        self.grid = Grid()
    
    def set_grid(self,width,height):
        self.grid.create_new(width,height)
        
    def mark_lost(self,x,y,index):
        self.grid.mark_x(x,y,index)
        
    def on_mars(self,x,y):
        return self.grid.in_bounds(x,y)
                
    def main(self):
        print('starting martians without interface')        
        
    def createMartian(self, x, y, d = Directions.N):
        self.martians.append(Martian([x, y], d, self))
        
    def setup(self):
        pass

if __name__ == '__main__':
    game = Martians()
    game.main()