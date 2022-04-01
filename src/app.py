from key_generator import KeyGenerator

print("\nRSA Encrypter / Decrypter")
print("Choose how many bit keys you want to use. "
        "\nMore bits more protection "
        "\n[1] 1024 bits\n[2] 2048 bits\n[3] 4096 bits")
while True:
    inp = int(input("> "))

    if inp == 1:
        B = 1024
        break
    if inp == 2:
        B = 2048
        break
    if inp == 3:
        B = 4096
        break
    print("False input")
kg = KeyGenerator(B)
public, private = kg.generate_keys()
print("DONE!")
