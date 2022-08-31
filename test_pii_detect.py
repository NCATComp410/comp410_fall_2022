import unittest
from pii_detect import show_aggie_pride


class Comp410TestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        # show_aggie_pride() returns a list of slogans
        result_list = show_aggie_pride()

        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        self.assertEqual(result_list[0], 'Aggie Pride - Worldwide')


if __name__ == '__main__':
    unittest.main()
