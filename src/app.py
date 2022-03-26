from key_generator import Key, KeyGenerator

print("\nRSA Encrypter / Decrypter")
print("Choose how many bit keys you want to use. \nMore bits more protection \n[1] 1024 bits\n[2] 2048 bits\n[3] 4096 bits")
while True:    
    inp = int(input("> "))

    if inp == 1:
        b = 1024
        break
    elif inp == 2:
        b = 2048
        break
    elif inp == 3:
        b = 4096
        break
    else:
        print("False input")
kg = KeyGenerator(b)
print("Howdy")
public, private = kg.generate_keys()

# print("PUBLIC KEY!: \n", public)
# print("\n")
# print("PRIVATE KEY!: \n", private)
