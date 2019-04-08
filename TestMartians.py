# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:44 2019

@author: Ilya Petin
"""
import unittest
from Martians import Martians, Directions, Commands


class TestDirection(unittest.TestCase):
    def test_directions(self):
        dirs = iter(Directions(["N", "E", "S","W"]))
        self.assertEqual(dirs.angle(),dirs.directions[0])
        
    def test_clockwise_rotation(self):
        dirs = iter(Directions(["N", "E", "S","W"]))
        self.assertEqual(next(dirs),dirs.directions[1])
        self.assertEqual(next(dirs),dirs.directions[2])
        self.assertEqual(next(dirs),dirs.directions[3])
        self.assertEqual(next(dirs),dirs.directions[0])
        self.assertEqual(next(dirs),dirs.directions[1])
        
    def test_counter_clockwise_ratation(self):  
        dirs = iter(Directions(["N", "E", "S","W"]))
        self.assertEqual(dirs.__prev__(),dirs.directions[3])
        self.assertEqual(dirs.__prev__(),dirs.directions[2])
        self.assertEqual(dirs.__prev__(),dirs.directions[1])
        self.assertEqual(dirs.__prev__(),dirs.directions[0])      
        self.assertEqual(dirs.__prev__(),dirs.directions[3])
    
    def test_martian_direction(self):
        game = Martians()
        game.setup()
        game.createMartian(0,0)
        self.assertEqual(game.martians[-1].direction.angle(), "N")
        game.createMartian(0,0,"W")
        self.assertEqual(game.martians[-1].direction.angle(), "W")
    
class TestCommands(unittest.TestCase):
    def test_default_values(self):
      #  game = Martians()
      #  game.createMartian(0,0)
      #  martian = game.martians[-1]
        commands = Commands()
        self.assertEqual(commands.command_exists("L"), True)   
        
    
class TestMartians:    
    def main(self):
       unittest.main()    

if __name__ == '__main__':
    unittest.main()