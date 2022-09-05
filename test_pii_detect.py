import unittest
from pii_detect import show_aggie_pride


class Comp410TestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        # show_aggie_pride() returns a list of slogans
        result_list = show_aggie_pride()

        # make sure a list is returned
        self.assertIsInstance(result_list, list)

        # make sure there is at least one aggie in the list
        has_aggie = False
        for slogan in result_list:
            if 'Aggie' in slogan:
                has_aggie = True
                break
        self.assertTrue(has_aggie, 'No Aggie slogans found')

        # make sure the list has the expected number of slogans
        self.assertEqual(4, len(result_list), 'Unexpected number of slogans')

    def test_ap_ww(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[0], 'Aggie Pride - Worldwide')

    def test_aggies_go(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[2], 'Go Aggies')
        
    def test_aggie_do(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[1], 'Aggies Do!')

    def test_aggie_proud(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[3], 'We are Aggies!')
        

if __name__ == '__main__':
    unittest.main()
