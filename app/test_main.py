"""
A simple and incomplete test script for main.py in this directory
Run as

    python app/test_main.py

http://www.diveintopython3.net/unit-testing.html
http://www.drdobbs.com/testing/unit-testing-with-python/240165163
https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html
"""

import main
import unittest
from utils import config_utils
config = config_utils.load_yaml_config()


class HelloWorld(unittest.TestCase):

    known_values = config['example']['hello_world_string']

    def test_to_hello_world_known_values(self):
        # hello_world should give known result with known input

        expected_string = self.known_values
        result = main.hello()
        self.assertEqual(expected_string, result)


if __name__ == '__main__':
    unittest.main()
