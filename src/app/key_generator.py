import math
import random

# This class provides functions and utilities to create proper public and private keys for RSA-system
class KeyGenerator:
    def __init__(self, bits):
        self.bits = bits
        self.public_key = None
        self.private_key = None
        self.e = None

    # This function creates one set of public and private key
    def generate_keys(self):
        p, q = self.generate_primes()
        mod = p * q                                         ## Calculate modulus
        lambd = abs((p-1)*(q-1)) // math.gcd((p-1), (q-1))  ## Calculate lambda using Charmichaels function
        self.e = 65537                                      ## Exponent for public key
        exp = pow(self.e, -1, lambd)                        ## Calculate exponent for private key
        self.public_key = Key(mod, self.e)                  ## Create public key
        self.private_key = Key(mod, exp)                    ## Create private key
        return self.public_key, self.private_key

    # This function generates and returns two different prime numbers
    # implementation of Sieve of Eratosthenes
    def generate_primes(self):
        while True:
            p = random.getrandbits(self.bits // 2)
            if p % 2 == 0:
                continue
            if self.is_prime(p):
                break
        while True:
            q = random.getrandbits(self.bits // 2)
            if q % 2 == 0 or q == p:
                continue
            if self.is_prime(q):
                break
        return (p, q)

    # This function checks for primality of an integer at most 40 times
    # Implementation of Miller-Rabin algorithm
    def is_prime(self, n: int):
        k = 40

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        d, s = 0, n - 1
        while s % 2 == 0:
            d += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x in (1, n - 1):
                continue
            for _ in range(d - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

# This class provides utility to handle key-objects
class Key:
    def __init__(self, mod, exp):
        self.modulus = mod
        self.exponent = exp

    # This function returns the modulus of the key
    def get_mod(self):
        return self.modulus

    # This function returns the exponent of the key
    def get_exp(self):
        return self.exponent
