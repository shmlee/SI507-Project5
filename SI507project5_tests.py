import unittest
from SI507project5_code import *

class Part1(unittest.TestCase):
	def setUp(self):
		self.followers = open('followers.csv', 'r')
		self.chocolate = open('chocolate.csv','r')
	def read_files(self):
		self.assertTrue(self.followers.read())
		self.assertTrue(self.chocolate.read())
	def tearDown(self):
		self.followers.close()
		self.chocolate.close()














if __name__ == "__main__":
    unittest.main(verbosity=2)
