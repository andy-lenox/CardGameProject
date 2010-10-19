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
		if self.number_of_cards >= 40:
			self.cards = card_list
			self.deck = copy.copy(self.cards)
			return True
			
	def shuffle(self):
		if self.discard:
			cards.append(discard)
			del discard[:]
		random.shuffle(cards)
		
	def cards_remaining(self):
		return len(self.deck)
		
	def print_deck(self):
		print self.deck
			
class deckTests(unittest.TestCase):
	def setUp(self):
		self.d = deck()
		
	def test_build_deck(self):
		card_list = []
		for x in range(40):
			card_list.append(random.randint(0,6))
		self.assertTrue(self.d.build_deck(card_list))
		del card_list[:]
		for x in range(39):
			card_list.append(random.randint(0,6))
		self.assertTrue(not self.d.build_deck(card_list))
		
	def test_shuffle(self):
		pass

if __name__ == '__main__':
	unittest.main()