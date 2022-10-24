from pickle import FALSE
import unittest
from unittest import result
from pii_team_frost import *


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
        lst = ["123-45-6789"]
        message = " - US SSN Lists Dont Match"
        self.assertEqual(results_list, lst, message)

        # Test for multiple US SSN within a given sentance
        results_list = find_us_ssn('My friends social security is 245-57-8359, and my other friends social security is 678-52-4878')
        lst2 = ["245-57-8359", "678-52-4878"]
        message = " - US SSN Lists Dont Match"
        self.assertEqual(results_list, lst2,message)

        # Test for invalid case where SSN was not in right format
        results_list = find_us_ssn('My Social Security is 23-56-4576')
        message = " - Invalid SSN Format"
        self.assertFalse(results_list, message)


    def test_find_email(self):
        results_list = find_email('My email address is jim.jones@jones.com')
        self.assertEqual(results_list, [])

    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @jimjones')
        self.assertEqual(results_list, [])


if __name__ == '__main__':
    unittest.main()
