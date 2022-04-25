from builtins import ValueError, int, print
from key_generator import KeyGenerator
from encrypt_decrypt import Encrypt, Decrypt

def __init__():
    pass

def launch():
    print("\n*****RSA Encrypter / Decrypter*****")

    while True:
        print("Choose how many bit keys you want to use. "
              "\nMore bits more protection "
              "\n[1] 1024 bits\n[2] 2048 bits\n[3] 4096 bits")
        try:
            bits = int(input("> "))
        except ValueError:
            print("****Please give proper input****\n")
            continue

        if bits == 1:
            bits = 1024
            break
        if bits == 2:
            bits = 2048
            break
        if bits == 3:
            bits = 4096
            break
        print("False input.", type(bits))

    print("\nGenerating keys...\n")
    key_generator = KeyGenerator(bits)
    public, private = key_generator.generate_keys()
    encrypted_message = None

    print("Keys generated!")

    while True:
        print("\n[1] Encypt a message\n[2] Decrypt a message\n[3] Stop")

        try:
            command1_from_user = int(input("> "))
        except ValueError:
            print("****Please give proper input****\n")
            continue

        if command1_from_user == 1:
            print("\nType in message to be encrypted:")
            message = input("> ")
            msg_size = len(message.encode())
            encrypted_message = Encrypt().encrypt_message(message, public)
            print(message, " in encrypted form ", encrypted_message)
        if command1_from_user == 2:
            print("\n[1] Copy previously encrypted message to be decrypted\n[2] Stop")
            try:
                command2_from_user = int(input("> "))
            except ValueError:
                print("****Please give proper input****\n")
                continue
            if command2_from_user == 1:
                if not encrypted_message == None:
                    decrypted_message = Decrypt().decrypt_message(encrypted_message, msg_size, private)
                    print("\nDecrypted message: ", decrypted_message)
                else:
                    print("\nEncrypted message could not be found, please try again")
            if command2_from_user == 2:
                break
        if command1_from_user == 3:
            break

launch()
