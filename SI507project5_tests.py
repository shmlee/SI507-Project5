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
		pass


class Part2(unittest.TestCase):
	def setUp(self):
		pass
	def test_list_vars(self):
		self.assertIsInstance(tumblr_rows, list)
		self.assertIsInstance(tumblr_rows2, list)
	def test_types(self):
		self.assertEqual(type(tag), type(""))
	def test_list_types(self):
		self.assertIsInstance(tumblr_result2, dict)
		self.assertIsInstance(tumblr_result3, dict)
	
	










if __name__ == "__main__":
    unittest.main(verbosity=2)
