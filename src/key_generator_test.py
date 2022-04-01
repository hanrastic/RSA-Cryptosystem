import unittest

from key_generator import KeyGenerator


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.keygenerator = KeyGenerator(1024)
    def test_key_generation(self):
        self.keygenerator.generate_keys()
        self.assertEqual(True, self.keygenerator.public_key is not None)
        self.assertEqual(True, self.keygenerator.private_key is not None)

    def test_prime_number_generation(self):
        p,q = self.keygenerator.generate_primes()
        self.assertEqual(True, self.keygenerator.is_prime(p))
        self.assertEqual(True, self.keygenerator.is_prime(q))

    def test_is_prime_function(self):
        self.assertEqual(True, self.keygenerator.is_prime(3700889))
        self.assertEqual(True, self.keygenerator.is_prime(982805851549327779922977967973))
        self.assertEqual(True, self.keygenerator.is_prime(7))
        self.assertEqual(True, self.keygenerator.is_prime(328054627542497))
        self.assertEqual(True, self.keygenerator.is_prime(2))

    def test_is_not_prime_function(self):
        self.assertEqual(False, self.keygenerator.is_prime(9))
        self.assertEqual(False, self.keygenerator.is_prime(213))
        self.assertEqual(False, self.keygenerator.is_prime(1245443))
        self.assertEqual(False, self.keygenerator.is_prime(38299301928383102938213098))
