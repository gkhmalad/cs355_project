import os
import binascii

# Large prime number
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF

# Generator is taken as 2
g = 2

"""
    KEYGEN
"""
# Secret key Alice
x = int(binascii.hexlify(os.urandom(128)), base=16)

# Public Key (p, g, h, G)
h = pow(g, x, p)

"""
    ENCRYPTION
"""
# Custom message and its hex counterpart
msg = input("Enter the message: ")
hexMSG = msg.encode('utf-8').hex()

# Secret Key Bob
y = int(binascii.hexlify(os.urandom(128)), base=16)

# Shared Secret Bob
s = pow(h,y,p)

c1 = pow(g, y, p)
c2  = pow((int(hexMSG, 16) * s), 1, p)

print(c1)
print(c2)

"""
    DECRYPTION
"""
# Given parameters are only c1 and c2
# Alice calculates shared secret
sAlice = pow(c1, x, p)

sInverse = pow(sAlice, -1, p)

m = pow((c2 * sInverse), 1, p)

print(bytes.fromhex(hex(m)[2:]).decode('utf-8'))