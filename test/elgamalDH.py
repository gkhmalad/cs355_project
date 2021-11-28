import os
import binascii

p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF

# Generating a key
def keygen():

    return int(binascii.hexlify(os.urandom(32)), base=16)

# Creating a public exponent
def public_exponent(secretKey, p):
    
    g = 2

    return pow(g, secretKey, p)

# Creating a shared key
def sharedKey(publicExponent, secretKey, p):

    return pow(publicExponent, secretKey, p)

alice = keygen()
bob = keygen()

print(public_exponent(bob, p))
print(public_exponent(alice, p))

print(sharedKey(public_exponent(alice, p), bob, p) == sharedKey(public_exponent(bob, p), alice, p))