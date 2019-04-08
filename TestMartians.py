# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:44 2019

@author: Ilya Petin
"""
import unittest
from Martians import Martians


class TestMartianInit(unittest.TestCase):
    game = Martians()
    expected_pos = ["N", "S", "E", "W"]
    
    def test_directions(self):
        self.game.setup()
        self.assertEqual(self.game.directions.pos(),self.expected_pos[0])
        
    def test_clockwise_rotation(self):
        self.game.setup()
        self.assertEqual(next(self.game.directions),self.expected_pos[1])
        self.assertEqual(next(self.game.directions),self.expected_pos[2])
        self.assertEqual(next(self.game.directions),self.expected_pos[3])
        self.assertEqual(next(self.game.directions),self.expected_pos[0])
        
    def test_counter_clockwise_ratation(self):        
        self.game.setup()
        self.assertEqual(self.game.directions.__prev__(),self.expected_pos[3])
        self.assertEqual(self.game.directions.__prev__(),self.expected_pos[2])
        self.assertEqual(self.game.directions.__prev__(),self.expected_pos[1])
        self.assertEqual(self.game.directions.__prev__(),self.expected_pos[0])      
        self.assertEqual(self.game.directions.__prev__(),self.expected_pos[3])
        
class TestMartians:    
    def main(self):
       unittest.main()    

if __name__ == '__main__':
    unittest.main()