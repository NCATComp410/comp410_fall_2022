import unittest
import re
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
        self.assertEqual(25, len(result_list), 'Unexpected number of slogans')


    def test_starts_with_test(self):
        # In order to run as a test case the method name must start with test
        # This test checks to make sure all defines within this file start with test
        # This is a common mistake that can cause tests to be skipped
        with open('test_pii_detect.py') as f:
            for line in f:
                # make sure everything that looks like a method name starts with test
                m = re.search(r'\s*def (\w+)', line)
                if m:
                    self.assertTrue(m.group(1).startswith('test'),
                                    'Method name does not start with test: def ' + m.group(1))

    def test_ap_ww(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[0], 'Aggie Pride - Worldwide')

    def test_aggie_do(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[1], 'Aggies Do!')

    def test_aggies_go(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[2], 'Go Aggies')

    def test_aggie_proud(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[3], 'We are Aggies!')

    def test_thats_on_1891(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[4], 'Thats on 1891!')

    def test_whataggiesdo(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[5], 'Thats What Aggies Do!')

    def test_letsgoaggies(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[6], 'Lets Go Aggies!')

    def test_aggies_skate(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[7], 'Aggies skate, Aggies grind!')

    def test_show_aggies(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[8], 'Show em what Aggies do')

    def test_aggie_born(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[9], 'Aggie born, Aggie bred')

    def test_aggies_stick(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[10], 'Aggies stick together')
        
    def test_NeverUnderestimate_MoveForward(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[11], 'Never Ever Underestimate An Aggie. Move Forward With Purpose.')

    def test_aggie_for_life(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[12], 'Aggie For Life!')
        
    def test_new_aggie_slogan(self):
       result_list = show_aggie_pride()
       self.assertEqual(result_list[13], 'Go Aggie Pride!')
    
    def test_Aggie_National(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[14], 'Aggie Nation!')

    def test_Aggie_Achieve(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[15], 'Aggies Achieve!')

    def test_Aggie_Go(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[16], 'Aggies Go!')


    def test_aggie_what_pride_what(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[17], 'Aggie what? Pride what give me that, give me that')

    def test_its_ghoe_baby(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[18], 'It\'s GHOE Babyyy!')

    def test_aggies_periodt_ahh(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[19], 'Aggies are periodt ahh, Eagles are periodt ugh')


    def test_aggies_rule(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[20], 'Aggies Rule, Eagles Drool')
        
    def test_aggie_what(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[21], 'A G G I E what!')

    def test_aggie_dead(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[22], 'And when I die, I am Aggie Dead!')

    def test_Aggies_learn(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[23], 'Aggies Learn')


if __name__ == '__main__':
    unittest.main()
