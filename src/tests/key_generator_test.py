import unittest

from app.key_generator import KeyGenerator


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.keygenerator = KeyGenerator(1024)
        self.public, self.private = self.keygenerator.generate_keys()

    def test_key_generation(self):
        self.assertEqual(True, self.keygenerator.public_key is not None)
        self.assertEqual(True, self.keygenerator.private_key is not None)

    def test_prime_number_generation(self):
        public, private = self.keygenerator.generate_primes()
        self.assertEqual(True, self.keygenerator.is_prime(public))
        self.assertEqual(True, self.keygenerator.is_prime(private))

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

    def test_keys(self):
        self.assertEqual(self.public, self.keygenerator.public_key)
        #self.assertEqual(True, self.keygenerator.is_prime(self.keygenerator.public_key))
        self.assertEqual(self.private, self.keygenerator.private_key)
        #self.assertEqual(True, self.keygenerator.is_prime(self.keygenerator.private_key))
