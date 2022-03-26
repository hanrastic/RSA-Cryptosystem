import math
import random

class Key:
    def __init__(self, mod, exponent):
        self.modulus = mod
        self.exponent = exponent
    def get_key(self):
        return self.modulus, self.exponent

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
        print("Toimii!")
        self.public_key = Key(mod, e)
        self.private_key = Key(mod, exp)
        print(self.public_key.get_key, self.private_key.get_key)
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
        #Uses miller-rabin algorithm for primality testing. Runs the test at most k times
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0: return False

        k = 40
        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        for _ in range(k):
            a = random.randrange(2, n-1)
            x = a ** d % n
            if x == 1: continue
            for _ in range(s):
                if x == n-1: break
                x = x**2 % n
            else:
                return False
        return True
    

        

