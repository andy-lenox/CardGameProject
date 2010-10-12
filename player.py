#!/usr/bin/env python
# encoding: utf-8
"""
player.py

Created by Andrew Lenox on 2010-10-12.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import deck


class player:
	def __init__(self):
		self.deck = deck.deck()
		self.playerNumber = None


class playerTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()