#!/usr/bin/env python
# encoding: utf-8
"""
play_area.py

Created by Andrew Lenox on 2010-10-10.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import math

import stack

class play_area:
	def __init__(self):
		self.p1Stack = stack.stack()
		self.p2Stack = stack.stack()
		
	def compare(self):
		return math.fabs( self.p1Stack.top() - self.p2Stack.top() )
		
	def clear(self):
		self.p1Stack.clear()
		self.p2Stack.clear()
		
	def clearP1Pile(self):
		discard = []
		for x in self.p1Stack:
			discard.append(self.p1Stack.pop())
		return discard
	
	def clearP2Pile(self):
		discard = []
		for x in self.p2Stack:
			discard.append(self.p2Stack)
		return discard

class play_areaTests(unittest.TestCase):
	def setUp(self):
		self.play = play_area()
		
	def test_setup(self):
		p = self.play
		p.p1Stack.push(1)
		p.p2Stack.push(1)
		# 1-1 should be 0
		self.assertEqual(0,p.compare())
		
	def test_clear(self):
		p = self.play
		for x in range(10):
			p.p1Stack.push(x)
			p.p2Stack.push(x)
		self.assertEqual(10, p.p1Stack.size())
		self.assertEqual(10, p.p1Stack.size())
		p.clear()
		self.assertEqual(0, p.p1Stack.size())
		self.assertEqual(0, p.p1Stack.size())
	
	def test_clearPiles(self):
		p = self.play
		for x in range(10):
			p.p1Stack.push(x)
			p.p2Stack.push(x)
		discard = p.clearP1Pile()
		index = 0
		for card in discard:
			assertEqual(index, card)
			index += 1
		


if __name__ == '__main__':
	unittest.main()