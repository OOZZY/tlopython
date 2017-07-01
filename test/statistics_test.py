import unittest
import tlo.statistics
import sys

EPSILON = sys.float_info.epsilon

class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.statistics = tlo.statistics.Statistics()

  def test_statistics_init_should_initialize_statistics(self):
    self.assertAlmostEqual(self.statistics.size, 0, delta = EPSILON)
    self.assertIsNone(self.statistics.sum)
    self.assertIsNone(self.statistics.mean)
    self.assertIsNone(self.statistics.min)
    self.assertIsNone(self.statistics.max)
    self.assertIsNone(self.statistics.range)
    self.assertIsNone(self.statistics.variance)
    self.assertIsNone(self.statistics.stddeviation)

  def test_statistics_add_should_update_statistics_over_one_call(self):
    self.statistics.add(50.0)
    self.assertAlmostEqual(self.statistics.size, 1, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.sum, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.mean, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.min, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.max, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.range, 0, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.variance, 0, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.stddeviation, 0, delta = EPSILON)

  def test_statistics_add_should_update_statistics_over_multiple_calls(self):
    self.statistics.add(50.0)
    self.statistics.add(100.0)
    self.assertAlmostEqual(self.statistics.size, 2, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.sum, 150, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.mean, 75, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.min, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.max, 100, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.range, 50, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.variance, 625, delta = EPSILON)
    self.assertAlmostEqual(self.statistics.stddeviation, 25, delta = EPSILON)

if __name__ == '__main__':
  unittest.main()
