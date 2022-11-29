import unittest
from pii_team_frost import *
from pii_detect import find_city_state, find_account_number, anonymize_pii


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

class Comp410TestPII(unittest.TestCase):
    def test_find_city_state(self):
        # Test a single city and state
        result_list = find_city_state('I live in Houston, TX')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test two cities and states
        result_list = find_city_state('I have lived in Houston, TX and Dallas, TX')
        self.assertEqual(result_list[0], 'Houston, TX')
        self.assertEqual(result_list[1], 'Dallas, TX')

        # Test beginning of string
        result_list = find_city_state('Houston, TX is a great city')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test middle of string
        result_list = find_city_state('I lived in Houston, TX for 10 years')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test an invalid case where the state is not capitalized
        result_list = find_city_state('I live in houston, TX')
        # result_list should be empty
        self.assertFalse(result_list)

        # Test a two-word city
        result_list = find_city_state('I live in New York, NY')
        self.assertEqual(result_list[0], 'New York, NY')

        # Test an invalid state abbreviation
        # TODO - it is currently not a requirement to support invalid state abbreviations
        # result_list = find_city_state('I live in Houston, AA')
        # result_list should be empty
        # self.assertFalse(result_list)

    def test_find_account_number(self):
        # Test a single account number
        result_list = find_account_number('My account number is 1234567890')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number at start of string
        result_list = find_account_number('1234567890 is my account number')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number in middle of string
        result_list = find_account_number('My account 1234567890 is not active')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number at end of string
        result_list = find_account_number('My account number is 1234567890')
        self.assertEqual(result_list[0], '1234567890')

        # Test multiple account numbers
        result_list = find_account_number('My account numbers are 1234567890 and 0987654321')
        self.assertEqual(result_list[0], '1234567890')
        self.assertEqual(result_list[1], '0987654321')

        # Test account number with dashes
        result_list = find_account_number('My account number is 123-456-7890')
        # Dashes are not supported
        self.assertFalse(result_list)

    def test_replace_name(self):
        test_str = 'My name is John Edwards'
        expected = 'My name is <PERSON>'
        result = anonymize_pii(test_str)
        self.assertEqual(expected, result.text)

    def test_replace_account_number(self):
        test_str = 'My account numbers are 123-12345 and 1234-12345'
        expected = 'My account numbers are <ACCOUNT_NUMBER> and <ACCOUNT_NUMBER>'
        result = anonymize_pii(test_str)
        self.assertEqual(expected, result.text)

    def test_replace_credit_card(self):
        test_str = 'My cc is 4095-3434-2424-1414'
        expected = 'My cc is <CREDIT_CARD>'
        result = anonymize_pii(test_str)
        self.assertEqual(expected, result.text)

    def test_replace_nothing(self):
        test_str = 'I am not going to tell you what my name is'
        expected = 'I am not going to tell you what my name is'
        result = anonymize_pii(test_str)
        self.assertEqual(expected, result.text)

    def test_replace_multiple(self):
        test_str = '750-12-1234 and 4095-3434-2424-1414 and 919-555-1212'
        expected = '<US_SSN> and <CREDIT_CARD> and <PHONE_NUMBER>'
        result = anonymize_pii(test_str)
        self.assertEqual(expected, result.text)

if __name__ == '__main__':
    unittest.main()
