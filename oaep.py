import hashlib
from ntpath import join
from operator import xor
import random
from re import A

#mensagem original hasheada
hasher = hashlib.sha3_224()
hasher.update(b"teste")              #224 bits, 28by  
teste =  hasher.digest()


def padding(m):
    compr = len(m)   
    pad = b'\x00' * (32 - compr)       # G - menos compr
    return m+pad


def g_hashing(m):
    hasheador = hashlib.sha256()
    hasheador.update(m)              #256 bits, 32by  G
    return hasheador.digest()

def h_hashing(m):
    hasheador = hashlib.sha1()
    hasheador.update(m)              #160bits, 20by   H)
    return hasheador.digest()
    pass

def xorlist(m1,m2):
    m3 =[]
    for i in range(len(m1)):
        m3.append(m1[i]^m2[i])
    return m3

def oeap_encrypt(m):

    m_pad = padding(m)   #padding na mensagem
    r = random.getrandbits(160)                          # nounce aleatorio h bits
    r = r.to_bytes(20,"big")
    r_hasheado = g_hashing(r)    #hash g no nounce

    r_hash_arr = (bytearray(r_hasheado))
    m_pad_arr = (bytearray(m_pad))

    X = xorlist(r_hash_arr,m_pad_arr)

    x_hasheado = h_hashing(bytearray(X))

    x_hash_arr = bytearray(x_hasheado)
    r_arr = bytearray(r)
    Y = xorlist(r_arr,x_hash_arr)

    #print(X)
    #print(Y)
    #print(r)
    #print(m_pad)

    return joincharlist(X+Y)
   

def oaep_decrypt(m):
    XY = voltalistastr(m)
    X = XY[:32]
    Y = XY[32:]

    x_hasheado = h_hashing(bytearray(X))   #reaplica hash no X
    x_hash_arr = bytearray(x_hasheado)

    x_arr = bytearray(X)
    y_arr = bytearray(Y)
    r = bytearray(xorlist(y_arr,x_hash_arr))  

    r_hasheado = g_hashing(r)    #reaplica hash no r


    m_pad = bytearray(xorlist(r_hasheado,x_arr))  

    #print(X)
    #print(Y)
    #print(r)
    #print(m_pad)

    return m_pad[:28]





def joincharlist(l):
    return ''.join(chr(i) for i in l)

def voltalistastr(s):
    return [ord(c) for c in s]

oaep_teste = oeap_encrypt((teste))
#print(oaep_teste)
print(oaep_decrypt(oaep_teste))