import unittest
import tlo.util
import platform

class TestUtil(unittest.TestCase):
  def test_print_python_version_should_return_the_version_of_python(self):
    self.assertEqual(tlo.util.print_python_version(), platform.python_version())

if __name__ == '__main__':
  unittest.main()
