from email import message
from key_generator import KeyGenerator
from encrypt_decrypt import Encrypt, Decrypt

def __init__(self):
        pass

def launch():
    print("\nRSA Encrypter / Decrypter")
    print("Choose how many bit keys you want to use. "
            "\nMore bits more protection "
            "\n[1] 1024 bits\n[2] 2048 bits\n[3] 4096 bits")
    while True:
        bits = int(input("> "))

        if bits == 1:
            bits = 1024
            break
        if bits == 2:
            bits = 2048
            break
        if bits == 3:
            bits = 4096
            break
        print("False input")
    
    kg = KeyGenerator(bits)
    public, private = kg.generate_keys()

   
    while True:
        print("\n[1]Encypt a message\n[2]Decrypt a message\n[3]Stop")
        command1_from_user = int(input("> "))

        if command1_from_user == 1:
            print("\nType in message to be encrypted:")
            message = input("> ")
            msg_size= len(message.encode())
            encrypted_message = Encrypt().encrypt_message(message, public)
            print(message, " in encrypted form ", encrypted_message)
        if command1_from_user == 2:
            print("\n[1] Copy previously encrypted message to be decrypted\n[2] Stop")
            command2_from_user = int(input("> "))
            if command2_from_user == 1:
                decrypted_message = Decrypt().decrypt_message(encrypted_message, msg_size, private)
                print("\nDecrypted message: ", decrypted_message)
            if command2_from_user == 2:
                break
        if command1_from_user == 3:
            break
                

launch()


# if __name__ == "__main__":
#     pass

# def __init__(self):
#     self.keys_generated = False
#     self.public, self.private = None
#     self.kg = KeyGenerator()

# def launch():
#     print("\nRSA Encrypter / Decrypter")
#     print("Choose how many bit keys you want to use. "
#             "\nMore bits more protection "
#             "\n[1] 1024 bits\n[2] 2048 bits\n[3] 4096 bits")
#     while True:
#         inp = int(input("> "))

#         if inp == 1:
#             bits = 1024
#             break
#         if inp == 2:
#             bits = 2048
#             break
#         if inp == 3:
#             bits = 4096
#             break
#         print("False input")
    
#     generate(bits)

#     print("\n[1]Encypt a message\n[2]Decrypt a message")
#     while True:
#         inp = input("> ")

#         if inp == 1:
#             pass

# def generate(self, bits: int):
#     try:
#         self.kg = KeyGenerator(bits)
#         self.public, self.private = self.kg.generate_keys()
#         self.keys_generated = True
#     except:
#         print("Key generation failed")

# launch()
