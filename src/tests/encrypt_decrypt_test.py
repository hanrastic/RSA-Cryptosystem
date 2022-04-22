import unittest
from app.key_generator import KeyGenerator
from app.encrypt_decrypt import Encrypt, Decrypt


class TestEncrypt(unittest.TestCase):
    def setUp(self):
        self.keygenerator = KeyGenerator(1024)
        self.public, self.private = self.keygenerator.generate_keys()
        self.test_message = "This is an example message to be encrypted."
        self.test_message2 = "This is an example message to be encrypteb."
        self.test_message_length = len(self.test_message.encode())
        self.encrypted_message = Encrypt().encrypt_message(self.test_message, self.public)
        self.decrypted_message = None

    def test_encrypting(self):
        self.assertEqual(type(self.encrypted_message), int)

    def test_decrypting(self):
        self.decrypted_message = Decrypt().decrypt_message(self.encrypted_message, self.test_message_length, self.private)
        self.assertEqual(self.decrypted_message, self.test_message)
        self.assertNotEqual(self.decrypted_message, self.test_message2)
        