import math
import random

class Key:
    def __init__(self, mod, exp):
        self.modulus = mod
        self.exponent = exp

    def get_mod(self):
        return self.modulus

    def get_exp(self):
        return self.exponent

class KeyGenerator:
    def __init__(self, bits):
        self.bits = bits
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        p, q = self.generate_primes()
        mod = p * q                                         ##Calculate modulus
        lambd = abs((p-1)*(q-1)) // math.gcd((p-1), (q-1))  ##Calculate lambda
        self.e = 65537                                      ##Exponent for public key
        exp = pow(self.e, -1, lambd)                        ##Calculate exponent for private key
        self.public_key = Key(mod, self.e)
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
