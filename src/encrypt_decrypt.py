from key_generator import KeyGenerator, Key

class Encrypt:

    def encrypt_message(self, message, key):
        bytes = message.encode()
        i_int = int.from_bytes(bytes, 'big')
        encrypted_msg = pow(i_int, key.get_exp(), key.get_mod())
        return encrypted_msg


class Decrypt:

    def decrypt_message(self, message, size, key):
        decrypted_msg = pow(message, key.get_exp(), key.get_mod())
        bytes = decrypted_msg.to_bytes(size, 'big')
        text = bytes.decode()
        return text