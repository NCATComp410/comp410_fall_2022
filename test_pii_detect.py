import unittest
from pii_detect import find_city_state


class Comp410TestPII(unittest.TestCase):
    def test_find_city_state(self):
        # Test a single city and state
        result_list = find_city_state('I live in Houston, TX')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test two cities and states
        result_list = find_city_state('I have lived in Houston, TX and Dallas, TX')
        self.assertEqual(result_list[0], 'Houston, TX')
        self.assertEqual(result_list[1], 'Dallas, TX')

        # Test beginning of string
        result_list = find_city_state('Houston, TX is a great city')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test middle of string
        result_list = find_city_state('I lived in Houston, TX for 10 years')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test an invalid case where the state is not capitalized
        result_list = find_city_state('I live in houston, TX')
        # result_list should be empty
        self.assertFalse(result_list)

        # Test a two-word city
        result_list = find_city_state('I live in New York, NY')
        self.assertEqual(result_list[0], 'New York, NY')

        # Test an invalid state abbreviation
        # TODO - it is currently not a requirement to support invalid state abbreviations
        # result_list = find_city_state('I live in Houston, AA')
        # result_list should be empty
        # self.assertFalse(result_list)


if __name__ == '__main__':
    unittest.main()
