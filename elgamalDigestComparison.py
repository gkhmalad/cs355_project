import os
import binascii
import hashlib
import hmac
import digester

# Primitive constants from a cyclic group
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF

g = 2


# Returns a 128 bit random key
def keygen():
    return int(binascii.hexlify(os.urandom(128)), base=16)

# Elgamal encryption scheme
def encrypt_signed(msg, h):

    hexMSG = msg.encode('utf-8').hex()
    y = keygen()
    s = pow(h,y,p)
    c1 = pow(g, y, p)
    c2  = pow((int(hexMSG, 16) * s), 1, p)
    signature = sign(s,c2)

    return c1,c2,signature

def decrypt(c1, c2, x):

    s = pow(c1, x, p)
    sInv = pow(s, -1, p)
    mInt = pow((c2 * sInv), 1, p)

    return mInt

def sign(sharedSecret, cipher):

    return hmac.new(str(sharedSecret).encode(), str(cipher).encode(), hashlib.sha3_256).hexdigest()

def signature_validator(c1, c2, signature, secretKey):

    # Recalculate signature with own private key
    sharedSecret = pow(c1, secretKey, p)
    newSignature = hmac.new(str(sharedSecret).encode(), str(c2).encode(), hashlib.sha3_256).hexdigest()

    return newSignature == signature


def main():
    print("\n========================================================")
    print("Simulating a message exchange between Alice and Bob")
    print("Bob and alice want to be sure they have the same value without revealing even the digest of the value")
    print("========================================================\n")

    # Alice generates a private key 'x' and a public key 'h'
    x = keygen()
    h = pow(g, x, p)

    # Bob generates a private key 'y' and a public key 'k'
    y = keygen()
    k = pow(g,y,p)

    # Bob inputs a message, and encrypts it to send to alice
    valueAlice = digester.file_digest("./passwords.txt")
    valueBob = digester.file_digest("./passwords.txt")

    # Encrypting both sides
    b1,b2,signatureB = encrypt_signed(valueBob,k)
    a1,a2,signatureA = encrypt_signed(valueAlice, k)

    # Homomorphic division with modular inverse
    divVal1 = (b1*pow(a1, -1, p))
    divVal2 = (b2*pow(a2, -1, p))

    bobsMSG = decrypt(divVal1,divVal2,y)
    
    if(bobsMSG == 1):
        print("The two values are the same!")
    else:
        print("The two values are NOT the same!")

    # This is repeated for Alice as well!


if __name__=="__main__":
    main()