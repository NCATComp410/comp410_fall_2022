import unittest
from pii_team_t2 import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list, [])  # add assertion here

    def test_find_visa_mastercard(self):
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list[0], "1234-5678-9012-3456")

        results_list = find_visa_mastercard('1234-5678-9012-3456 is my credit card number')
        self.assertEqual(results_list[0], "1234-5678-9012-3456")

        results_list = find_visa_mastercard('The number, 1234-5678-9012-3456, could be my credit card number')
        self.assertEqual(results_list[0], "1234-5678-9012-3456")

        results_list = find_visa_mastercard('The number, 1234-5678-9012-3456, is my credit card number, '
                                            'but 3245-7397-9275-2643, and 9432-7849-7234-2987 are my old numbers.')
        self.assertEqual(results_list[0], "1234-5678-9012-3456")
        self.assertEqual(results_list[1], "3245-7397-9275-2643")
        self.assertEqual(results_list[2], "9432-7849-7234-2987")


    def test_find_amex(self):
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list, [])

    def test_find_us_ssn(self):
        results_list = find_us_ssn('My social security number is 123-45-6789')
        self.assertEqual(results_list, [])

    def test_find_email(self):
        results_list = find_email('My email address is jim.jones@jones.com')
        self.assertEqual(results_list, [])

    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @jimjones')
        self.assertEqual(results_list, [])


if __name__ == '__main__':
    unittest.main()
