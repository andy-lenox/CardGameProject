#!/usr/bin/env python
# encoding: utf-8
"""
stack.py

Created by Andrew Lenox on 2010-09-21.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest


class stack: #Using a list as a stack
	def __init__(self):
		self.p = []
		self.index = 0
		
	def __iter__(self):
		return self
	
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.p[self.index]
		
	def push(self,t):
		self.p.append(t)
			
	def pop(self):
		return self.p.pop()
		
	def top(self):
		if self.p:
			return self.p[-1]
		
	def remove(self):
		self.p.pop(0)
	
	def clear(self):
		while self.size() > 0:
			self.p.pop()
		
	def isEmpty(self):
		return (len(self.p)==0)
		
	def printStack(self):
		print self.p
		
	def isFull(self):
		return (len(self.p) >= 5)
				
	def size(self):
		return len(self.p)
	
	def equal(self, s):
		return self.p == s.p
		
class stackTests(unittest.TestCase):
	def setUp(self):
		self.s = stack()
	
	def test_iterable(self):
		stack = self.s
		stack.push(1)
		stack.push(2)
		stack.push(3)
		i = 1
		for s in stack:
			self.assertEqual(i, s)
			i -= 1
			
	def test_clear(self):
		stack = self.s
		stack.push(1)
		stack.push(2)
		stack.push(3)
		self.assertTrue(stack.size() == 3)
		stack.clear()
		self.assertTrue(stack.size() == 0)

if __name__ == '__main__':
	unittest.main()