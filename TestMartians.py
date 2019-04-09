# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:44 2019

@author: Ilya Petin
"""
import unittest
from Martians import Martians, Directions, Commands, Grid


class TestDirection(unittest.TestCase):
    def test_directions(self):
        dirs = Directions(["N", "E", "S","W"])
        self.assertEqual(dirs.facing(),dirs.directions[0])
        
    def test_clockwise_rotation(self):
        dirs = Directions(["N", "E", "S","W"])
        self.assertEqual(dirs.right(),dirs.directions[1])
        self.assertEqual(dirs.right(),dirs.directions[2])
        self.assertEqual(dirs.right(),dirs.directions[3])
        self.assertEqual(dirs.right(),dirs.directions[0])
        self.assertEqual(dirs.right(),dirs.directions[1])
        
    def test_counter_clockwise_ratation(self):  
        dirs = Directions(["N", "E", "S","W"])
        self.assertEqual(dirs.left(),dirs.directions[3])
        self.assertEqual(dirs.left(),dirs.directions[2])
        self.assertEqual(dirs.left(),dirs.directions[1])
        self.assertEqual(dirs.left(),dirs.directions[0])      
        self.assertEqual(dirs.left(),dirs.directions[3])
    
    def test_martian_direction(self):
        game = Martians()
        game.setup()
        game.createMartian(0,0)
        self.assertEqual(game.martians[-1].direction.facing(), "N")
        game.createMartian(0,0,"W")
        self.assertEqual(game.martians[-1].direction.facing(), "W")
    
class TestCommands(unittest.TestCase):        
    def test_left_command(self):
        dirs = Directions(["N", "E", "S","W"])
        game = Martians()
        game.createMartian(0,0)
        martian = game.martians[-1]
        martian.execute_command("L")
        self.assertEqual(martian.facing(),dirs.directions[1])
        
    def test_right_command(self):
        dirs = Directions(["N", "E", "S","W"])
        game = Martians()
        game.createMartian(0,0)
        martian = game.martians[-1]
        martian.execute_command("R")
        self.assertEqual(martian.facing(),dirs.directions[3])    
 
class TestGrid(unittest.TestCase):
    def test_grid_build(self):
        grid = Grid()
        grid.create_new(5)
        self.assertEqual(grid.grid[0][1],0)  
        self.assertEqual(grid.grid[4][4],0)
        
    def test_forward_north_command(self):
        game = Martians()
        game.createMartian(0,0,"N")
        self.assertEqual(len(game.martians),1)
        martian = game.martians[-1]
        martian.execute_command("F")
        self.assertEqual(martian.x,0)
        self.assertEqual(martian.y,1) 
        
    def test_forward_east_command(self):
        game = Martians()
        game.createMartian(0,0,"E")
        self.assertEqual(len(game.martians),1)
        martian = game.martians[-1]
        martian.execute_command("F")
        self.assertEqual(martian.x,1)
        self.assertEqual(martian.y,0) 
        
    def test_forward_west_command(self):
        game = Martians()
        game.createMartian(1,0,"W")
        self.assertEqual(len(game.martians),1)
        martian = game.martians[-1]
        martian.execute_command("F")
        self.assertEqual(martian.x,0)
        self.assertEqual(martian.y,0) 
     
    def test_forward_south_command(self):
        game = Martians()
        game.createMartian(0,1,"S")
        self.assertEqual(len(game.martians),1)
        martian = game.martians[-1]
        martian.execute_command("F")
        self.assertEqual(martian.x,0)
        self.assertEqual(martian.y,0)  
    
    def test_bounds(self):
        grid = Grid()
        grid.create_new(51)
        self.assertEqual(grid.in_bounds(0,50),True) 
        
    def test_lost(self):
        game = Martians()
        game.createMartian(0,0,"N")
        grid = Grid()
        grid.create_new(3)
        game.grid = grid

        self.assertEqual(len(game.martians),1)
        martian = game.martians[-1]
        martian.execute_command("F")
        self.assertEqual(martian.y,1)  
        martian.execute_command("F")
        self.assertEqual(martian.y,2) 
        martian.execute_command("F")
        self.assertEqual(martian.y,2)
        self.assertEqual(martian.is_lost,True)
        #cant move twice to the same location
        game.createMartian(0,0,"N")
        martian2 = game.martians[-1]
        martian2.execute_command("F")
        self.assertEqual(martian2.y,1)  
        martian2.execute_command("F")
        self.assertEqual(martian2.y,1) 
        martian2.execute_command("F")
        self.assertEqual(martian2.y,1)
        self.assertEqual(martian2.is_lost,False)        
                         
class TestMartians:    
    def main(self):
       unittest.main()    

if __name__ == '__main__':
    unittest.main()