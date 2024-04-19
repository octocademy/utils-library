import unittest
import utils

class TestValidationMethods(unittest.TestCase):

    def test_is_email_valid(self):
        self.assertTrue(utils.is_email_valid('test@github.com'))
        self.assertFalse(utils.is_email_valid('invalid_string'))

    def test_is_phone_valid(self):
        self.assertTrue(utils.is_phone_valid('4255552368'))
        self.assertFalse(utils.is_phone_valid('invalid_string'))

    def test_is_secure_url_valid(self):
        self.assertTrue(utils.is_secure_url_valid('https://example.com'))
        self.assertFalse(utils.is_secure_url_valid('http://example.com'))
        self.assertFalse(utils.is_secure_url_valid('invalid_string'))

    def test_is_github_url_valid(self):
        self.assertTrue(utils.is_github_url_valid('https://github.com/octocademy/utils-library'))
        self.assertFalse(utils.is_github_url_valid('https://example.com'))
        self.assertFalse(utils.is_github_url_valid('invalid_string'))

if __name__ == '__main__':
    unittest.main()
