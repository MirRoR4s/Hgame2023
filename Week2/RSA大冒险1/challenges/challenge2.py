from Crypto.Util.number import *
from challenges import chall2_secret

class RSAServe:
    def __init__(self) -> None:
        self.p = getPrime(512)
        self.q = getPrime(512)
        self.e = 65537
        self.m = chall2_secret
    
    def encrypt(self):
        m_ = bytes_to_long(self.m)
        c = pow(m_ ,self.e, self.p*self.q)
        self.q = getPrime(512)
        return hex(c)

    def check(self, msg):
        return msg == self.m

    def pubkey(self):
        return self.p*self.q, self.e