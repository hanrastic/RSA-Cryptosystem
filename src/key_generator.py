import math
import random

class Key:
    def __init__(self, mod, exponent):
        self.modulus = mod
        self.exponent = exponent

class KeyGenerator:
    def __init__(self, bits):
        #bits joko 1024, 2048 tai 4096
        self.bits = bits
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        p, q = self.generate_primes()
        mod = p * q                         ##Calculate modulus
        lambd = abs(p*q) // math.gcd(p, q)  ##Calculate lambda
        e = 65537                           ##Exponent for public key
        exp = pow(e, -1, lambd)             ##Calculate exponent for private key
        self.public_key = Key(mod, e)
        self.private_key = Key(mod, exp)
        return self.public_key, self.private_key

    def generate_primes(self):
        #Primes p & q so that p != q
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
