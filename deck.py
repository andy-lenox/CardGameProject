#!/usr/bin/env python
# encoding: utf-8
"""
deck.py

Created by Andrew Lenox on 2010-10-12.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import copy
import random

class deck:
	def __init__(self):
		self.cards = None
		self.deck = None
		self.discard = None
		self.number_of_cards = None

	def build_deck(self, card_list):
		self.number_of_cards = len(card_list)
		if number_of_cards >= 40:
			self.cards = card_list
			self.deck = cards.copy()
			
	def shuffle(self):
		if self.discard:
			cards.append(discard)
			del discard[:]
		random.shuffle(cards)
			
class deckTests(unittest.TestCase):
	def setUp(self):
		self.d = deck()
		
	def test_build_deck(self):
		pass
		
	def test_shuffle(self):
		pass

if __name__ == '__main__':
	unittest.main()