import unittest
from Tools import *


class ToolsTests(unittest.TestCase):

  def test_getNthFibonacciTerm(self):
    expected = [(-1, 0), (0, 0), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8)]
    for exp in expected:
      result = getNthFibonacciTerm(exp[0])
      self.assertEqual(exp[1], result)

  def test_getNextCollatzTerm(self):
    expected = [(0, 0), (1, 4), (2, 1), (3, 10), (4, 2)]
    for exp in expected:
      result = getNextCollatzTerm(exp[0])
      self.assertEqual(exp[1], result)

  def test_getNthTriangleTerm(self):
    expected = [(0, 0), (1, 1), (2, 3), (3, 6)]
    for exp in expected:
      result = getNthTriangleTerm(exp[0])
      self.assertEqual(exp[1], result)

  def test_getPrimeComponents_primeNumbers(self):
    expected = [1, 2, 3, 5, 7, 11, 101]
    for exp in expected:
      result = getPrimeComponents(exp)
      self.assertEqual(1, len(result))
      self.assertEqual(exp, result[0])

  def test_getPrimeComponents_compositeNumbers(self):
    expected = [(4, (2, 2)),
          (6, (2, 3)),
          (8, (2, 2, 2)),
          (9, (3, 3)),
          (10, (5, 2)),
          (25, (5, 5)),
          (30, (2, 3, 5)),
          (72, (2, 3, 2, 3, 2)),
          (75, (3, 5, 5)),
          (202, (2, 101)),
          (3030, (2, 3, 5, 101)),
          (367236, (2, 2, 3, 3, 101, 101))]
    for exp in expected:
      result = getPrimeComponents(exp[0])
      self.assertEqual(len(exp[1]), len(result))
      for p in exp[1]:
        self.assertTrue(result.__contains__(p))
        result.remove(p)

  def test_isPrime_returnsCorrectResult(self):
    expected = [(-2, False),
          (-1, False),
          (0, False),
          (1, False),
          (2, True),
          (3, True),
          (4, False),
          (5, True),
          (6, False),
          (7, True),
          (8, False),
          (9, False),
          (10, False),
          (11, True),
          (12, False),
          (13, True),
          (14, False),
          (17, True),
          (18, False),
          (19, True),
          (23, True),
          (100, False),
          (101, True)]
    for exp in expected:
      result = isPrime(exp[0])
      self.assertEqual(exp[1], result)

  def test_getNthPrimeNumber(self):
    expected = [(-1, 0),
          (0, 0),
          (1, 2),
          (2, 3),
          (3, 5),
          (4, 7),
          (5, 11),
          (6, 13),
          (8, 19),
          (10, 29)]
    for exp in expected:
      result = getNthPrimeNumber(exp[0])
      self.assertEqual(exp[1], result)

  def test_getFactors_primeNumbers(self):
    expected = [2, 3, 5, 7, 11, 101]
    for exp in expected:
      result = getFactors(exp)
      self.assertEqual(2, len(result))
      self.assertTrue(result.__contains__(1))
      self.assertTrue(result.__contains__(exp))

  def test_getFactors_compositeNumbers(self):
    expected = [(1, (1, )),
          (4, (1, 2, 4)),
          (6, (1, 2, 3, 6)),
          (8, (1, 2, 4, 8)),
          (9, (1, 3, 9)),
          (10, (1, 5, 2, 10)),
          (24, (1, 2, 3, 4, 6, 8, 12, 24)),
          (25, (1, 5, 25)),
          (30, (1, 2, 3, 5, 6, 10, 15, 30)),
          (36, (1, 2, 3, 4, 6, 9, 12, 18, 36)),
          (202, (1, 2, 101, 202))]
    for exp in expected:
      result = getFactors(exp[0])
      self.assertEqual(len(exp[1]), len(result))
      for p in exp[1]:
        self.assertTrue(result.__contains__(p))

  def test_isPalindrome_numbers(self):
    expected = [(1, True),
          (6, True),
          (11, True),
          (12, False),
          (101, True),
          (111, True),
          (121, True),
          (122, False),
          (1221, True),
          (1232, False),
          (12321, True),
          (12345, False)]
    for exp in expected:
      result = isPalindrome(exp[0])
      self.assertEqual(exp[1], result)

  def test_isPalindrome_strings(self):
    expected = [("a", True),
          ("C", True),
          ("aa", True),
          ("Aa", False),
          ("ab", False),
          ("aba", True),
          ("aaa", True),
          ("aZa", True),
          ("abb", False),
          ("abba", True),
          ("abca", False),
          ("abcba", True),
          ("abcde", False),
          ("tacocat", True),
          ("Tacocat", False)]
    for exp in expected:
      result = isPalindrome(exp[0])
      self.assertEqual(exp[1], result)


if __name__ == '__main__':
  unittest.main()
