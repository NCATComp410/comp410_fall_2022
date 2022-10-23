import unittest
from pii_team_sei import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list, [])  # add assertion here

    def test_find_visa_mastercard(self):
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list, [])

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
    
        # Test an alphabetical token
        result_list = find_instagram_handle('My instagram handle is @classicman')
        self.assertEqual(result_list[0], '@classicman')

        # Test a case-insensitive token
        result_list = find_instagram_handle('My instagram handle is @ClassicMan')
        self.assertEqual(result_list[0], '@ClassicMan')

        # Test an alphanumeric token
        result_list = find_instagram_handle('My instagram handle is @cl4ssicm4n')
        self.assertEqual(result_list[0], '@cl4ssicm4n')

        # Test token with an enclosed underscore
        result_list = find_instagram_handle('My instagram handle is @classic_man')
        self.assertEqual(result_list[0], '@classic_man')

        # Test token with leading/trailing underscore(s)
        result_list = find_instagram_handle('My instagram handle is @_classicman_')
        self.assertEqual(result_list[0], '@_classicman_')

        # Test token with an enclosed period
        result_list = find_instagram_handle('My instagram handle is @classic.man')
        self.assertEqual(result_list[0], '@classic.man')

        # Test token with leading/trailing period(s)
        result_list = find_instagram_handle('My instagram handle is @.classicman.')
        self.assertEqual(result_list[0], '@.classicman.')

        # Test a single account number
        result_list = find_instagram_handle('My instagram handle is @_.classicman._')
        self.assertEqual(result_list[0], '@_.classicman._')

        # Test that emails do not match
        result_list = find_instagram_handle('My email is classicman@outlook.com')
        self.assertFalse(result_list)

        # Test that no character can precede the handle
        result_list = find_instagram_handle('My email is:@outlook.com')
        self.assertFalse(result_list)


if __name__ == '__main__':
    unittest.main()
