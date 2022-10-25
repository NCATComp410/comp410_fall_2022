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
        # Test an alphabetical token
        result_list = find_instagram_handle('My instagram handle is @masterchief')
        self.assertEqual(result_list[0], '@masterchief')

        # Test a case-insensitive token
        result_list = find_instagram_handle('My instagram handle is @MasterChief')
        self.assertEqual(result_list[0], '@MasterChief')

        # Test an alphanumeric token
        result_list = find_instagram_handle('My instagram handle is @m4st3rch1ef')
        self.assertEqual(result_list[0], '@m4st3rch1ef')

        # Test token with an enclosed underscore
        result_list = find_instagram_handle('My instagram handle is @master_chief')
        self.assertEqual(result_list[0], '@master_chief')

        # Test token with leading/trailing underscore(s)
        result_list = find_instagram_handle('My instagram handle is @_masterchief_')
        self.assertEqual(result_list[0], '@_masterchief_')

        # Test token with an enclosed period
        result_list = find_instagram_handle('My instagram handle is @master.chief')
        self.assertEqual(result_list[0], '@master.chief')

        # Test token with leading/trailing period(s)
        result_list = find_instagram_handle('My instagram handle is @.masterchief.')
        self.assertEqual(result_list[0], '@.masterchief.')

        # Test a single account number
        result_list = find_instagram_handle('My instagram handle is @_.masterchief._')
        self.assertEqual(result_list[0], '@_.masterchief._')

        # Test that emails do not match
        result_list = find_instagram_handle('My email is john117@outlook.com')
        self.assertFalse(result_list)

        # Test that no character can precede the handle
        result_list = find_instagram_handle('My email is:@outlook.com')
        self.assertFalse(result_list)

if __name__ == '__main__':
    unittest.main()
