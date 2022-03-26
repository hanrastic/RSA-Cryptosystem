import unittest

from key_generator import KeyGenerator, Key

class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.keygenerator = KeyGenerator(1024)
    
    def test_is_prime_function(self):

        self.assertEqual(True, self.keygenerator.is_prime(3700889))

    def test_is_not_prime_function(self):

        self.assertEqual(False, self.keygenerator.is_prime(213))

