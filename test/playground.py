# message to be sent
p = 35

# public base
a =5

# N
modulo = 89

# bobs secret key component
r = 8

# alices secret key component
s = 13

# bobs public key
publicB = pow(a, r, modulo)
# alices secret key
publicA = pow(a, s, modulo)


# shared key bob
bobSharedKey = pow(publicA, r, modulo)
# shared key alice
aliceSharedKey = pow(publicB, s, modulo)
# these two should be equal
print(bobSharedKey == aliceSharedKey)

# computing ciphertext
ciphertext = (p * bobSharedKey)%modulo
print(ciphertext)