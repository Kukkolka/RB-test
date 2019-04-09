# -*- coding: utf-8 -*-
"""
Run this file
"""
from TestMartians import TestMartians
from Interface import Controller
from Martians import Martians

if __name__ == '__main__':
    test_martians = TestMartians()
    test_martians.main()
    app = Controller(Martians())