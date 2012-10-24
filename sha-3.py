#! /usr/bin/python3

#Copyright (c) 2012 E Brown
__author__ = 'Eliot Brown <eliotjbrown@gmail.com>'

#The SHA-3 (Keccak) reference is available online: http://keccak.noekeon.org/Keccak-reference-3.0.pdf
# --------"-------- implementation -------"------: http://keccak.noekeon.org/Keccak-implementation-3.2.pdf
#While the Keccak reference suggests using compact comments, to aid readability, I haven't!

import math as m

#from reprlib import repr //Not needed

#Width 					Hamming weight
#   	4 	6 		8 		10 			12 			14
#25 	825 12100 	95600 	465690 		1456725 	?
#50 	150 13835 	905135 	22392676 	?	 		?
#100 	48 	2712 	137078 	6953033 	? 			?
#200 	10 	481 	24037 	1143550 	56824109 	?
#400 	4 	83 		4006 	164806 		7290847		?
#800 	0 	28 		918 	30771 		1154855 	44788752
#1600 	0 	10 		304 	8231 		259567 		8399589
#
#Buffer must conform to b is in set {25, 50, 100, 200, 400, 800, 1600}

class sha3Exc(Exception):
	'''Error as listed in the implementation guide'''
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value) //Limit string length - hence use of repr

class sha3:
	'''Main class implementation of the Keccak hashing function'''
	
	def __init__(self, b=1600)
		"""Set b to 1600 as standard, though it can be {25, 50, 100, 200, 400, 800, 1600}"""
		self.setValB(b)

	def setValB(b)
		"""Set the value of b (the width of the permutation) """
		if b is not [25, 50, 100, 200, 400, 800, 1600]:
			raise sha3Exc.sha3Exc('b needs to be 25, 50, 100, 200, 400, 800 or 1600')
