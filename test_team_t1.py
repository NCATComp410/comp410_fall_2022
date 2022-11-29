import unittest
from pii_team_t1 import *


class TeamFrostTests(unittest.TestCase):
    def test_find_us_phone_number(self):
        # test a single phone number at the end of a string
        results_list = find_us_phone_number('My phone number is 123-456-7890')
        self.assertEqual(results_list[0], '123-456-7890')

        # test a single phone number at the beginning of a string
        results_list = find_us_phone_number('123-456-7890 is my phone number')
        self.assertEqual(results_list[0], '123-456-7890')

        # test a single phone number in the middle of a string
        results_list = find_us_phone_number('You can reach me at 123-456-7890. That is my number')
        self.assertEqual(results_list[0], '123-456-7890')

        # test multiple phone numbers
        results_list = find_us_phone_number('123-456-7890 is my phone number. Her number is 987-654-3210')
        self.assertEqual(results_list[0], '123-456-7890')
        self.assertEqual(results_list[1], '987-654-3210')

        # test an invalid phone number
        results_list = find_us_phone_number('1234567890 is my phone number')
        # result_list should be empty
        self.assertFalse(results_list)

    def test_find_visa_mastercard(self):
        # return results at end of string
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9012-3456')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')

        # return results at beginning of string
        results_list = find_visa_mastercard('1234-5678-9012-3456 is my credit card number')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')

        # return results with multiple numbers
        results_list = find_visa_mastercard(
            'I have 2 cards. one number is 1234-5678-9012-3456 the other is 3210-9876-5432-1098')
        self.assertEqual(results_list[0], '1234-5678-9012-3456')
        self.assertEqual(results_list[1], '3210-9876-5432-1098')

        # test wrong format
        results_list = find_visa_mastercard('My credit card number is 1234-5678-3456')
        self.assertFalse(results_list)

        # test with letter inside
        results_list = find_visa_mastercard('My credit card number is 1234-5678-9TF2-3456')
        self.assertFalse(results_list)

    def test_find_amex(self):
        results_list = find_amex('My credit card number is 1234-567890-12345')
        self.assertEqual(results_list[0], '1234-567890-12345')

        # return results in middle of string
        results_list = find_amex('My new card number is 1234-567890-54321. This is a new card')
        self.assertEqual(results_list[0], '1234-567890-54321')

        # return wrong number format
        results_list = find_amex('The card number is 1234-5678-90123')
        self.assertFalse(results_list)

        # return number from end of string
        results_list = find_amex('Her card number is 0987-654321-23456')
        self.assertEqual(results_list[0], '0987-654321-23456')

    def test_find_us_ssn(self):
        results_list = find_us_ssn('My social security number is 123-45-6789')
        self.assertEqual(results_list[0], '123-45-6789')

        # tests with a SSN at the end of the string
        results_list = find_us_ssn('My social security number is 123-45-6789')
        self.assertEqual(results_list[0], '123-45-6789')

        # tests with a SSN at the beginning of a string
        results_list = find_us_ssn('123-45-6789 is my social security number')
        self.assertEqual(results_list[0], '123-45-6789')

        # tests with a SSN in the middle of a string
        results_list = find_us_ssn('Can the number 123-45-6789 be my new SSN')
        self.assertEqual(results_list[0], '123-45-6789')

        # tests with a different number for SSN
        results_list = find_us_ssn('My social security number is 012-01-0123')
        self.assertEqual(results_list[0], '012-01-0123')

        # tests with multiple SSN in the string
        results_list = find_us_ssn('Is my SSN 123-45-6789 or is 123-12-1234 my SSN')
        self.assertEqual(results_list[0], '123-45-6789')
        self.assertEqual(results_list[1], '123-12-1234')

        # tests SSN without dashes
        results_list = find_us_ssn('My SSN is 123456789')
        # US SSNs must have dashes after the third digit and after the 5th digit
        self.assertFalse(results_list)

        # tests with letters entered instead of digits
        results_list = find_us_ssn('my SSN is 123-four5-6789')
        self.assertFalse(results_list)

    def test_find_email(self):
        # test an email given at the end of string
        results_list = find_email("My email address is jim.jones@jones.com")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')

        # test an email given at the beginning of string
        results_list = find_email("jim.jones@jones.com is my email")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')

        # test multiple emails given
        results_list = find_email("My email address is jim.jones@jones.com , her's is sarahouston@gmail.com")
        self.assertEqual(results_list[0], 'jim.jones@jones.com')
        self.assertEqual(results_list[1], 'sarahouston@gmail.com')

        # test with new email address
        results_list = find_email("My new email addrees is panthers89@yahoo.com")
        self.assertEqual(results_list[0], 'panthers89@yahoo.com')

        # test invalid email
        results_list = find_email("My email address is jim.jones.com")
        self.assertFalse(results_list)

    def test_find_instagram_handle(self):
        # test an ig handle at the end of a string
        results_list = find_instagram_handle('My instagram handle is @jimjones')
        self.assertEqual(results_list, ['@jimjones'])
        # test an ig handle given at the beginning of a string
        results_list = find_instagram_handle('@jimjones is my instagram handle')
        self.assertEqual(results_list, ['@jimjones'])
        # test multiple ig handles given
        results_list = find_instagram_handle('My instagram handle is @jimjones. My cousin\'s is @caryjones.')
        self.assertEqual(results_list, ['@jimjones', '@caryjones'])
        # test with special characters handle
        results_list = find_instagram_handle('My instagram handle is @jim_jones')
        self.assertEqual(results_list, ['@jim_jones'])
        # test with an invalid ig handle given
        results_list = find_instagram_handle('My instagram handle is jimjones')
        self.assertEqual(results_list, [])

    def test_replace_us_phone_number(self):
        string = 'My phone number is 336-123-8945'
        convert = 'My phone number is <PHONE_NUMBER>'
        output = anonymize_pii(string)
        self.assertEqual(convert, output.results)


    def test_replace_us_ssn(self):
        string = 'My ssn is 123-45-6789'
        convert = 'My ssn is <US_SSN>'
        output = anonymize_pii(string)
        self.assertEqual(convert, output.results)



if __name__ == '__main__':
    unittest.main()
