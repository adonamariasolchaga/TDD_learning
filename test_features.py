from io import StringIO
import unittest

from compute_stats_refactor import *

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.int_list = [1,2,3,4]

    def test_harmonic_mean(self):
        self.assertAlmostEqual(harmonic_mean(self.int_list), 1.92)

    def test_variance(self):
        self.assertAlmostEqual(variance(self.int_list), 1.25)

    def test_standerd_dev(self):
        self.assertAlmostEqual(standard_dev(self.int_list), 1.118033989)

    def test_maximum(self):
        self.assertEqual(maximum(self.int_list), 4)

    def test_minimum(self):
        self.assertEqual(minimum(self.int_list), 1)

    def test_average(self):
        self.assertEqual(average(self.int_list), 2.5)

    def test_summation(self):
        self.assertEqual(summation(self.int_list), 10)

    def test_count(self):
        self.assertEqual(count(self.int_list), 4)
        
    def test_read_ints(self):
        # Mock content of the file as a string
        mock_file_content = '1\n2\n3\n4\n'
        # Use StringIO to simulate a file object with the mock content
        io_object = StringIO(mock_file_content)
        
        # Call the function to test with the StringIO object
        result = read_ints(io_object)
        
        # Assert the expected result
        self.assertEqual(result, self.int_list)
