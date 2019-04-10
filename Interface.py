# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 

@author: Ilya Petin
"""
from Martians import Martians, Directions
class Controller(object):
    
    def addRobot(self):
        robot_args = input("Enter Robot positions and orientation (N,W,S,E) \n")
        robot_str = robot_args.strip(' \t\n\r').split(" ")
        if len(robot_str) is not 3:
           raise Exception("Must have 3 values")      
        try:
            pos_x = int(robot_str[0])
            pos_y = int(robot_str[1])
        except:
            raise Exception("positions of the robot must be numberic values!")
            
        if not robot_str[2] in [Directions.N, 
                                Directions.E, 
                                Directions.S, 
                                Directions.W]:
                raise Exception("orientation of the robot must N,W,S,E")           
        
        commands = input("Enter robot commands (F, R, L) without whitespace: \n")
        commands_str = commands.strip(' \t\n\r')       
        self.game.createMartian(pos_x,pos_y,robot_str[2])
        robot = self.game.martians[-1]
        for command in commands_str:
            robot.execute_command(command)
        print(robot.x, robot.y,robot.facing(), robot.lost())
        
    def begin(self):
        dimention_args = input("Enter Grid dimentions seperated by whitespace e.g (5 3): \n")   
        dimention_str=dimention_args.strip(' \t\n\r').split(" ")
        dimentions = []
        if len(dimention_str) is not 2:
            raise Exception("Must have 2 values")
        for val in dimention_str:
            try:
                val = int(val)
                if val>50:
                    raise Exception("value too high")
                else:
                    dimentions.append(val)
            except Exception:
                raise Exception("All values must be numbers seperated by whitespace" )
                self.begin()
        try:
            if all(isinstance(x, int) for x in dimentions):
                self.game.set_grid(dimentions[0],dimentions[1])
            else:
                raise Exception("All values must be numbers seperated by whitespace 2")
                self.begin()
        except ValueError: 
            raise Exception("You havent entered correct values for dimentions")    
            self.begin()
        _continue = True
        self.robots = []
        while _continue:
            self.addRobot()
            
    def __init__(self,game):
        self.game = game
        self.begin()

    
if __name__ == '__main__':
    game = Martians()
    interface = Controller(game)