import unittest
import tlo.statistics
import sys

EPSILON = sys.float_info.epsilon

class TestStatistics(unittest.TestCase):
  def test_statistics_init_should_initialize_statistics(self):
    statistics = tlo.statistics.Statistics()
    self.assertAlmostEqual(statistics.size, 0, delta = EPSILON)
    self.assertIsNone(statistics.sum)
    self.assertIsNone(statistics.mean)
    self.assertIsNone(statistics.min)
    self.assertIsNone(statistics.max)
    self.assertIsNone(statistics.range)
    self.assertIsNone(statistics.variance)
    self.assertIsNone(statistics.stddeviation)

  def test_statistics_add_should_update_statistics_over_one_call(self):
    statistics = tlo.statistics.Statistics()
    statistics.add(50.0)
    self.assertAlmostEqual(statistics.size, 1, delta = EPSILON)
    self.assertAlmostEqual(statistics.sum, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.mean, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.min, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.max, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.range, 0, delta = EPSILON)
    self.assertAlmostEqual(statistics.variance, 0, delta = EPSILON)
    self.assertAlmostEqual(statistics.stddeviation, 0, delta = EPSILON)

  def test_statistics_add_should_update_statistics_over_multiple_calls(self):
    statistics = tlo.statistics.Statistics()
    statistics.add(50.0)
    statistics.add(100.0)
    self.assertAlmostEqual(statistics.size, 2, delta = EPSILON)
    self.assertAlmostEqual(statistics.sum, 150, delta = EPSILON)
    self.assertAlmostEqual(statistics.mean, 75, delta = EPSILON)
    self.assertAlmostEqual(statistics.min, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.max, 100, delta = EPSILON)
    self.assertAlmostEqual(statistics.range, 50, delta = EPSILON)
    self.assertAlmostEqual(statistics.variance, 625, delta = EPSILON)
    self.assertAlmostEqual(statistics.stddeviation, 25, delta = EPSILON)

if __name__ == '__main__':
  unittest.main()
