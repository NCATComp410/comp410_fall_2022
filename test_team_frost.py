
import unittest
from pii_team_frost import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        # test phone number at the end of a string
        results_list = find_us_phone_number('My phone number is 301-526-4113')
        self.assertEqual(results_list[0], '301-526-4113')

        # test phone number at the beginning of a string
        results_list = find_us_phone_number('123-456-7890 is my phone number')
        self.assertEqual(results_list[0], '123-456-7890')

        # test phone number in the middle of a string
        results_list = find_us_phone_number('You can reach me at 333-402-7890. That is my number')
        self.assertEqual(results_list[0], '333-402-7890')

        # test multiple phone numbers
        results_list = find_us_phone_number('123-456-7890 is my phone number. Her number is 987-654-3210')
        self.assertEqual(results_list[0], '123-456-7890')
        self.assertEqual(results_list[1], '987-654-3210')

        # test an invalid phone number
        results_list = find_us_phone_number('1234567890 is my phone number')
        self.assertFalse(results_list)

    def test_find_visa_mastercard(self):
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')

        results_list = find_visa_mastercard('1234-5678-9012-3456 is my credit card number')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')

        # more than one card number
        results_list = find_visa_mastercard('I have 2 cards. one number is 1234-5678-9012-3456 '
                                            'the other is 5489-1304-2985-7529')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')
        self.assertEqual(results_list[1], '5489-1304-2985-7529')

        # wrong format-credit card number incomplete
        results_list = find_visa_mastercard('My credit card number is 1234-5678-3456')
        self.assertFalse(results_list)

        # with a letter
        results_list = find_visa_mastercard('My credit card number is 1AB4-5678-9012-3456')
        self.assertFalse(results_list)

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
        # Test an alphanumeric email
        results_list = find_email('My email address is john117@unsc.gov')
        self.assertEqual(results_list[0], 'john117@unsc.gov')

        # Test a case-insensitive email
        results_list = find_email('My email address is John117@unsc.gov')
        self.assertEqual(results_list[0], 'John117@unsc.gov')

        # Test an email a period in the username
        results_list = find_email('My email address is john.117@unsc.gov')
        self.assertEqual(results_list[0], 'john.117@unsc.gov')

        # Test an email with an underscore in the username
        results_list = find_email('My email address is john_117@unsc.gov')
        self.assertEqual(results_list[0], 'john_117@unsc.gov')

        # Test an email with a second-level domain
        results_list = find_email('My email address is john117@unsc.gov.uk')
        self.assertEqual(results_list[0], 'john117@unsc.gov.uk')

        # Test an email with subaddressing
        results_list = find_email('My email address is john117+waypoint@unsc.com')
        self.assertEqual(results_list[0], 'john117+waypoint@unsc.com')

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

    def test_find_amex(self):
        # Test that number that doesn't start with a 34 or 37 is denied
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list, [])

        # Test that number with under 15 digits is denied
        results_list = find_amex('My credit card number is 1234-567890-1234')
        self.assertEqual(results_list, [])

        # Test that number with over 15 digits is denied
        results_list = find_amex('My credit card number is 1234-567890-123456')
        self.assertEqual(results_list, [])

        # Test that number starting with 34 is accepted
        results_list = find_amex('My credit card number is 3412-567890-12345')
        self.assertEqual(results_list, [])

        # Test that number starting with 37 is accepted
        results_list = find_amex('My credit card number is 3712-567890-12345')
        self.assertEqual(results_list, [])

if __name__ == '__main__':
    unittest.main()
