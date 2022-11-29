import unittest
from pii_team_sei import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        
        #test at the beginning of a string
        results_list = find_us_phone_number('123-456-7890 is my phone number')
        self.assertEqual(results_list[0], '123-456-7890')

        #test in the middle of a string
        results_list = find_us_phone_number('You can reach me at 123-456-7890. That is my number')
        self.assertEqual(results_list[0], '123-456-7890')
            
        #test multiple phone numbers
        results_list = find_us_phone_number('123-456-7890 is my phone number. Her number is 919-684-3210')
        self.assertEqual(results_list[0], '123-456-7890')
        self.assertEqual(results_list[1], '919-684-3210')
        
        #test at the end of a string
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list[0], '123-456-7890')
        
        #result_list should be empty
        self.assertFalse(results_list) 

    def test_find_visa_mastercard(self):
        #Not matching credit card number
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list, [])

        #Matching Visa credit card number
        results_list = find_visa_mastercard('My credit card number is 4234-5678-9012-3456')
        self.assertEqual(results_list[0], '4234-5678-9012-3456')

        #Matching Mastercard credit card number
        results_list = find_visa_mastercard('My credit card number is 5234-5678-9012-3456')
        self.assertEqual(results_list[0], '5234-5678-9012-3456')




    def test_find_amex(self):
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list, ['1234-567890-12345'])

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
