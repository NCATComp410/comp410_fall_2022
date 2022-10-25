import unittest
from pii_team_t2 import *


class TeamT2Tests(unittest.TestCase):
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
        
        results_list = find_email('My email address is jane-doe@mbc.com')
        self.assertEqual(results_list[0], 'jane-doe@mbc.com')

#return results at the beginning of string
results_list = find_email('jane-doe@mbc.com is my email address')
self.assertEqual(results_list[0], 'jane-doe@mbc.com')

#return results with multiple addresses
results_list = find_email('My email address is jane-doe@mbc.com')
self.assertEqual(results_list[0], 'jane-doe@mbc.com ')
self.assertEqual(results_list[1], 'doe-jane@mbc.com')

#return results for wrong formatting 
results_list = find_email('My email address is doe-jane@mbc.com')
self.assertFalse(results_list)

#return results with unneccessary characters
results_list = find_email('My email address is jane-doe;@mbc.com')
self.assertFalse(results_list)


    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @jimjones')
        self.assertEqual(results_list, [])


if __name__ == '__main__':
    unittest.main()
