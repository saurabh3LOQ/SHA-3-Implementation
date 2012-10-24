#! /usr/bin/python3

#Copyright (c) 2012 E Brown
__author__ = 'Eliot Brown <eliotjbrown@gmail.com>'

#The SHA-3 (Keccak) reference is available online: http://keccak.noekeon.org/Keccak-reference-3.0.pdf
# --------"-------- implementation -------"------: http://keccak.noekeon.org/Keccak-implementation-3.2.pdf
#While the Keccak reference suggests using compact comments, to aid readability, I haven't!

import math as m

#from reprlib import repr -- Not needed

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

class sha3Err(Exception):
	'''Error as listed in the implementation guide'''
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value) #Limit string length - hence use of repr

class sha3:
	'''Main class implementation of the Keccak hashing function
	''' 

	#Constants: Round constants (RC) and Rotation Offsets (RO)
	RC = [0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
		0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
		0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
		0x0000000000000088, 0x0000000080008009, 0x000000008000000A, 
		0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 
		0x8000000000008003, 0x8000000000008002, 0x8000000000000080, 
		0x000000000000800A, 0x800000008000000A, 0x8000000080008081, 
		0x8000000000008080, 0x0000000080000001, 0x8000000080008008]

	RO = [[0, 36, 3, 41, 18],
		[1, 44, 10, 45,	2],
		[62, 6,	43, 15,	61],
		[28, 55, 25, 21, 56],
		[27, 20, 39, 8,	14]]

	def __init__(self, b=1600):
		"""Set b to 1600, though it can be [25, 50, 100, 200, 400, 800, 1600]"""
		self.setValB(b)

	def setValB(b):
		"""Set the value of b (the width of the permutation) """
		if b is not [25, 50, 100, 200, 400, 800, 1600]:
			raise sha3Err.sha3Err('b needs to be 25, 50, 100, 200, 400, 800 or 1600')

		#Assign values to variables.
		self.b = b
		self.w = b//25 					#Number of bits long
		self.l = int(m.log(self.w, 2)) #Length of the message (in bits) - integer
		self.nr = 12+2*self.l


	def rotate(self, x, n):
		"""Bitwise rotation (anti-clockwise or left) of n bits
		Assign n as the remainder of n/w
		shift x right by w-n bits and left by n
		shift 1 left by w bits"""
		n = n%self.w
		return ((x>>(self.w-n))+(x<<n))%(1<<self.w)	

	def laneToHex(self, lane):
		"""Convert the lane value  into a string of bytes in hex"""
		laneHex = (("%%0%dX" % (self.w/4)) % lane) #%dX is decimal(int) hex value (uppercase)
		temporary = '' #Not only used temporarily but appears required
		numBytes = len(laneHex)/2
		for x in range (numBytes):
			offset = (numBytes-x-1)*2

	def hexToLane(self, string):
		"""Convert the hex string into a lane"""
		pass

	def printState(self, state, info):
		pass

	def stringToTable(self, string):
		pass	

	def tableToString(self, table):
		pass		

	def round(): #Not sure what the pass in variables are yet
		pass
