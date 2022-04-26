# Implementation Documentation

## Structure of the program
Core functionality is divided into 4 classes. 

1. Class `Key` is for handling and storing key objects
- Contains two methods: `get_mod()` which returns the modulus of the key and `get_exp()` which returns the exponent of the key.

2. Class `KeyGenerator` is for generating RSA-keypairs
- Contains three methods:
    - Method `generate_primes()` generates two different prime numbers
    - Method `is_prime()` checks the primality of the proposed numbers in method `generate_primes()`. Method is an implementation of Miller-Rabin primality test algorithm
    - Method `generate_keys()` creates one set of public and private keys. 

3. Class `Encrypt` is for encrypting a message
- Contains only one method `encrypt_message()` which is responsible of transforming the message in following order: string -> bytes -> integer

4. Class `Decrypt` is for decrypting an encrypted message
- Contains only one method `decrypt_message()` which is responsible of transforming the enctypted message in following order: integer -> bytes -> string 

## Time complexity
Time complexities reagarding the core functionality lies around the prime numbers.

- Primality checking via Miller-Rabin impelementation. Time complexity for the Miller-rabin ie. `is_prime()` method is O(k log^3 n). 
- Generating prime numbers method `generate_primes()` is an implementation of Sieve of Eratothenes. The time complexity for this is O(n log log n)

## Possible improvements in the future
Right now there really is no use case for this project. It is merely a proof of concept of the RSA -system. Maybe some web front for actually encrypting and decrypting messages could be nice.

## Sources
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [RSA(cryptosystem)](https://fi.wikipedia.org/wiki/RSA)
- [Miller-Rab](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
