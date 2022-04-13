# This class privides utility for encrypting messages
class Encrypt:

    # This function encryps a message using public key
    def encrypt_message(self, message, key):
        bytes = message.encode()                                    #Decodes message string into bytes
        i_int = int.from_bytes(bytes, byteorder = 'big')            #Integer from bytes
        encrypted_msg = pow(i_int, key.get_exp(), key.get_mod())    #Encrypts the message via; integer form of the message, exponent and modulus
        return encrypted_msg

# This class privides utility for encrypting messages
class Decrypt:

    # This function decrypts a message using private key
    def decrypt_message(self, message, size, key):
        decrypted_msg = pow(message, key.get_exp(), key.get_mod())  #Calculates the decrypted message via; decrypted message, exponet and modulus 
        bytes = self.int_to_bytes(decrypted_msg, size)              #Bytes from integer
        text = bytes.decode()                                       #Decodes bytes into text
        return text
    
    def int_to_bytes(self, msg_as_int, length):
        return msg_as_int.to_bytes(length, byteorder = "big")
