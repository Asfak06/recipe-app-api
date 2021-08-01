from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):

	def test_add_numbers(self):
		"""Testt that two numbers are added together"""
		self.assertEqual(add(3, 8), 11)

	def test_substract_numbers(self):
		"""Testt that two numbers are substracted"""
		self.assertEqual(substract(5, 11), 6)