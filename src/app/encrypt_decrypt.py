class Encrypt:
    def encrypt_message(self, message, key):
        bytes = message.encode()
        i_int = int.from_bytes(bytes, byteorder = 'big')
        encrypted_msg = pow(i_int, key.get_exp(), key.get_mod())
        return encrypted_msg

class Decrypt:
    def decrypt_message(self, message, size, key):
        decrypted_msg = pow(message, key.get_exp(), key.get_mod())
        bytes = self.int_to_bytes(decrypted_msg, size)
        text = bytes.decode()
        return text
    
    def int_to_bytes(self, msg_as_int, length):
        return msg_as_int.to_bytes(length, byteorder = "big")
