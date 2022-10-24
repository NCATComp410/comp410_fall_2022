import unittest
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
        self.assertEqual(results_list, [])

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

if __name__ == '__main__':
    unittest.main()
