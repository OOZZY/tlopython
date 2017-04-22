import unittest
import tlo.statistics

class TestStatistics(unittest.TestCase):
  def test_statistics_init_should_initialize_statistics(self):
    statistics = tlo.statistics.Statistics()
    self.assertEqual(statistics.size, 0)
    self.assertEqual(statistics.sum, None)
    self.assertEqual(statistics.mean, None)
    self.assertEqual(statistics.min, None)
    self.assertEqual(statistics.max, None)
    self.assertEqual(statistics.range, None)
    self.assertEqual(statistics.variance, None)
    self.assertEqual(statistics.stddeviation, None)

  def test_statistics_add_should_update_statistics_over_one_call(self):
    statistics = tlo.statistics.Statistics()
    statistics.add(50.0)
    self.assertEqual(statistics.size, 1)
    self.assertEqual(statistics.sum, 50)
    self.assertEqual(statistics.mean, 50)
    self.assertEqual(statistics.min, 50)
    self.assertEqual(statistics.max, 50)
    self.assertEqual(statistics.range, 0)
    self.assertEqual(statistics.variance, 0)
    self.assertEqual(statistics.stddeviation, 0)

  def test_statistics_add_should_update_statistics_over_multiple_calls(self):
    statistics = tlo.statistics.Statistics()
    statistics.add(50.0)
    statistics.add(100.0)
    self.assertEqual(statistics.size, 2)
    self.assertEqual(statistics.sum, 150)
    self.assertEqual(statistics.mean, 75)
    self.assertEqual(statistics.min, 50)
    self.assertEqual(statistics.max, 100)
    self.assertEqual(statistics.range, 50)
    self.assertEqual(statistics.variance, 625)
    self.assertEqual(statistics.stddeviation, 25)

if __name__ == '__main__':
  unittest.main()
