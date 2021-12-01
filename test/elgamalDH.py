import os
import binascii

p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF

g = 2

# Generating a key 128 or 80
def keygen():

    return int(binascii.hexlify(os.urandom(128)), base=16)

# Creating a public exponent
def public_exponent(secretKey, p, g):
    
    return pow(g, secretKey, p)

# Creating a shared key
def shared_key(publicExponent, secretKey, p):

    return pow(publicExponent, secretKey, p)

# Encryption algorithm
def enc(msg, modulo, receiverPublicExponent, publicBase, sendersPublicExponent):
    
    # ciphertext container
    c = []

    # calculate shared key
    sharedKey = pow(receiverPublicExponent, sendersPublicExponent, modulo)

    # copy msg characters into ciphertext container
    for i in range(0, len(msg)):
        c.append(msg[i])

    # multiply each characters int representative by the shared key
    for i in range(0, len(c)):
        c[i] = sharedKey * ord(c[i])

    return c

# Decryption algorithm
def dec(cipher, receiverPublicExponent, sendersPublicExponent, modulo):

    plaintext = []

    sharedKey = pow(receiverPublicExponent, sendersPublicExponent, modulo)

    for i in range(0, len(cipher)):
        plaintext.append(chr(int(cipher[i]/sharedKey)))

    return plaintext


def main():

    alice = keygen()
    print("\nAlice's private key: " + str(alice))

    bob = keygen()
    print("Bob's private key: " + str(bob))

    alicePublic = public_exponent(alice, p, g)
    print("\nAlices's public exponent:\n" + str(alicePublic))

    bobPublic = public_exponent(bob, p, g)
    print("\nBob's public exponent:\n" + str(bobPublic))

    message = str(input("\nEnter the message: "))

    print("\nCiphertext array:")
    ciphertext = enc(message, p, alicePublic, g, bobPublic)
    print(ciphertext)

    print("\nPlaintext array:")
    plaintext = dec(ciphertext, alicePublic, bobPublic, p)
    print(plaintext)


if __name__=="__main__":
    main()