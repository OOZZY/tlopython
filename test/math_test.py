import unittest
import tlo.math

class TestMath(unittest.TestCase):
  def test_factorial_should_return_n_factorial_when_given_n(self):
    self.assertEqual(tlo.math.factorial(0), 1)
    self.assertEqual(tlo.math.factorial(1), 1)
    self.assertEqual(tlo.math.factorial(2), 2)
    self.assertEqual(tlo.math.factorial(3), 6)
    self.assertEqual(tlo.math.factorial(4), 24)
    self.assertEqual(tlo.math.factorial(5), 120)
    self.assertEqual(tlo.math.factorial(6), 720)
    self.assertEqual(tlo.math.factorial(7), 5040)
    self.assertEqual(tlo.math.factorial(8), 40320)
    self.assertEqual(tlo.math.factorial(9), 362880)
    self.assertEqual(tlo.math.factorial(10), 3628800)

if __name__ == '__main__':
  unittest.main()
