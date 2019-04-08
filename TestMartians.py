# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:16:44 2019

@author: Ilya Petin
"""
import unittest
from Martians import Martians


class TestMartianInit(unittest.TestCase):
    martians = Martians()
    
    def test_setup(self):        
        self.assertEqual(self.martians.setup(),1)
        
    
class TestMartians:    
    def main(self):
       unittest.main()    

if __name__ == '__main__':
    unittest.main()