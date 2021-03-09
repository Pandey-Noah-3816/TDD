from leapyear import*
import unittest

class TestCase(unittest.TestCase):
  def test_case_1(self):
    self.assertEqual (leapyear(1921),False)
  def test_case_2(self):
    self.assertEqual (leapyear(2024),True)
  def test_case_3(self):
    self.assertEqual (leapyear(1900),False)





if __name__ == '__main__':unittest.main()
