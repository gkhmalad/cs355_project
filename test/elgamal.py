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

    return c[i]

# Decryption algorithm
def dec(cipher, modulo, sendersPublicExponent, sharedKey):

    plaintext = []

    for i in range(0, len(cipher)):
        plaintext.append(chr(int(cipher[i]/sharedKey)))


