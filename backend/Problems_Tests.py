import unittest
from Problems import *


class ProblemsTests(unittest.TestCase):

  def test_solve001_returnsCorrectResult(self):
    arg = 10
    expected = 23
    result = solve_001(arg)
    self.assertEqual(expected, result)

  def test_solve002_returnsCorrectResult(self):
    arg = 100
    expected = 44
    result = solve_002(arg)
    self.assertEqual(expected, result)

  def test_solve003_returnsCorrectResult(self):
    arg = 13195
    expected = 29
    result = solve_003(arg)
    self.assertEqual(expected, result)

  def test_solve004_returnsCorrectResultFor99(self):
    expected = 9009
    result = solve_004(99, 10)
    self.assertEqual(expected, result)

  def test_solve006_returnsCorrectResults(self):
    expected = [(1, 0),
          (2, 4),
          (10, 2640)]
    for exp in expected:
      result = solve_006(exp[0])
      self.assertEqual(exp[1], result)

  def test_solve008_returnsCorrectResult(self):
    expected = 5832
    result = solve_008(4)
    self.assertEqual(expected, result)

  def test_solve010_returnsCorrectResult(self):
    expected = 17
    result = solve_010(10)
    self.assertEqual(expected, result)


if __name__ == '__main__':
  unittest.main()
