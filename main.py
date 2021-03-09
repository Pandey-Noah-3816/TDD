from fizzbuzz import*
import unittest

class TestCase(unittest.TestCase):
  def test_case_1(self):
    self.assertEqual (fizzbuzz(1),1)
  def test_case_2(self):
    self.assertEqual (fizzbuzz(3),'fizz')
  def test_case_3(self):
    self.assertEqual (fizzbuzz(5),'buzz')



if __name__ == '__main__':unittest.main()
