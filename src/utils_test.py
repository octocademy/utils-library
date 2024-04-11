import unittest
import utils

class TestValidationMethods(unittest.TestCase):

    def test_is_email_valid(self):
        self.assertTrue(utils.is_email_valid('test@github.com'))
        self.assertFalse(utils.is_email_valid('invalid_string'))

    def test_is_phone_valid(self):
        self.assertTrue(utils.is_phone_valid('4255552368'))
        self.assertFalse(utils.is_phone_valid('invalid_string'))

if __name__ == '__main__':
    unittest.main()