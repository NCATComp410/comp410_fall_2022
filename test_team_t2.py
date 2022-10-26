import unittest
from pii_team_t2 import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list, ['123-456-7890'])  # add assertion here

    def test_find_visa_mastercard(self):
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list, [])

    def test_find_amex(self):
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list, [])

    def test_find_us_ssn(self):
        # Test a single SSN with dashes
        results_list = find_us_ssn('My social security number is 123-45-6789')
        self.assertEqual(results_list[0], '123-45-6789')

        # Test a single SSN without dashes
        results_list = find_us_ssn('My social security number is 123456789')
        self.assertEqual(results_list[0], '123456789')

        # Test SSN at start of string
        results_list = find_us_ssn('123456789 is my social security number.')
        self.assertEqual(results_list[0], '123456789')

        # Test SSN in middle of string
        results_list = find_us_ssn('My SSN 123456789 has been compromised.')
        self.assertEqual(results_list[0], '123456789')

        # Test SSN with dashes at end of string
        results_list = find_us_ssn('My SSN is 123-45-6789.')
        self.assertEqual(results_list[0], '123-45-6789')

        # Test multiple SSN within string
        results_list = find_us_ssn('My SSN is 123456789 and his is 987-65-4321.')
        self.assertEqual(results_list[0], '123456789')
        self.assertEqual(results_list[1], '987-65-4321')

    def test_find_email(self):
        results_list = find_email('My email address is jim.jones@jones.com')
        self.assertEqual(results_list, [])
    
    #testing alphabetical
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @ariorwateva')
        self.assertEqual(results_list[0], '@ariorwateva')
   
    #testing non case-sensitive
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @Ariorwateva')
        self.assertEqual(results_list[0], '@Ariorwateva')
   
    #testing non alphanumeric
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @ariorwateva25')
        self.assertEqual(results_list[0], '@ariorwateva25')
        
    #testing underscore
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @ariorwateva_')
        self.assertEqual(results_list[0], '@ariorwateva_')
    
    #testing '.'
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is @ari.orwateva')
        self.assertEqual(results_list[0], '@ari.orwateva')
        
    #testing invalid case with no @
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('My instagram handle is ariorwateva')
        self.assertFalse(results_list)
        
    def test_find_instagram_handle(self):
        results_list = find_instagram_handle('@ariorwateva is my IG')
        self.assertEqual(results_list[0], '@ariorwateva')
    

    

    


if __name__ == '__main__':
    unittest.main()
