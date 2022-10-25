import unittest
from pii_team_phantom import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list[0], '123-456-7890')  # add assertion here
        # tests email at the front
        results_list = find_us_phone_number("123-456-7890 is my phone number.")
        self.assertEqual(results_list[0], '123-456-7890')
        # tests 2 emails
        results_list = find_us_phone_number("123-456-7890 is my phone number, and 703-356-7643 is Jordan's.")
        self.assertEqual(results_list[0], '123-456-7890')
        self.assertEqual(results_list[1], '703-356-7643')
        # tests invalid email
        results_list = find_us_phone_number("My phone number is 1234567890")
        self.assertFalse(results_list)
    def test_find_visa_mastercard(self):
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list, [])

    def test_find_amex(self):
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list, [])

    def test_find_us_ssn(self):
        results_list = find_us_ssn('My social security number is 123-45-6789')
        self.assertEqual(results_list[0], '123-45-6789')

        #test SSN at the front
        results_list = find_us_ssn('123-45-6789 is my social security number')
        self.assertEqual(results_list[0], '123-45-6789')

        # test 2 SSN's
        results_list = find_us_ssn('123-45-6789 is my social security number and 987-65-4321 is my friends social security number')
        self.assertEqual(results_list[0], '123-45-6789')
        self.assertEqual(results_list[1], '987-65-4321')


    def test_find_email(self):
        # tests email at the end
        results_list = find_email("My email address is jim.jones@jones.com")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')
        # tests email at the front
        results_list = find_email("jim.jones@jones.com is my email address.")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')
        # tests 2 emails
        results_list = find_email("jim.jones@jones.com is my email address, and kemarsh@aggies.ncat.edu is Kennedy's.")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')
        self.assertEqual(results_list[1], 'kemarsh@aggies.ncat.edu')
        # tests invalid email
        results_list = find_email("My email address is jim.com")
        self.assertFalse(results_list)

    def test_find_instagram_handle(self):
        #handle with only letters
        results_list = find_instagram_handle('My instagram handle is @jimjones')
        self.assertEqual(results_list[0], '@jimjones')
        #handle with letters and digits
        results_list = find_instagram_handle('My instagram handle is @jimj0nes4')
        self.assertEqual(results_list[0], '@jimj0nes4')
        #handle with periods and underscore
        results_list = find_instagram_handle('My instagram handle is @jim.jones_')
        self.assertEqual(results_list[0], '@jim.jones_')
        #two handles
        results_list = find_instagram_handle('My instagram handle is @jimjones and my alt is @jonesjimmy')
        self.assertEqual(results_list[0], '@jimjones')
        self.assertEqual(results_list[1], '@jonesjimmy')
        #invalid handle
        results_list = find_instagram_handle('My instagram handle is @?imjones')
        self.assertFalse(results_list)



if __name__ == '__main__':
    unittest.main()
