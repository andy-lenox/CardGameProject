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
	def __init__(self, player_number, play_area):
		self.deck = deck.deck()
		self.playerNumber = player_number
		self.hand = []
		self.view = play_area
		self.hand_size = 5
		self.card_list = []
		
	def start(self):
		self.deck.build_deck(self.card_list)
		self.deck.shuffle()
		self.draw(self.hand_size)
		
	def draw(self, number):
		for x in range(number):
			if self.deck.cards_remaining() == 0:
				self.reset_deck()
			card = self.deck.draw()
			hand.append(card)

	def reset_deck():
		pass


class playerTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()