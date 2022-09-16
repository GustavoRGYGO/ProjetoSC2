import random 
import math
from millerrabin import gerador_primo

def gcd(a, b):
    assert a > b
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1 
        y0, y1 = y1, y0 - q * y1
    return b, y0, x0

def keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(1, phi - 1)
        if math.gcd(e, phi) == 1: 
            u, s, t = gcd(phi, e)
            if u == (s * phi + t * e):
                d = t % phi
                break
    
    
    publicKey = (e, n)
    privateKey = d
    return publicKey, privateKey


def main(): 
    p = gerador_primo(1024)
    q = gerador_primo(1024)
    publicKey, privateKey = keygen(p, q)
    print(publicKey)
    print(privateKey)
