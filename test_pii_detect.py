import unittest
from pii_detect import find_city_state, find_account_number, anonymize_pii


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
