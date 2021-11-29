import hashlib

# rb mode reads in binary, omits \n and such
with open("passwords.txt", 'rb') as file:
        data = file.read()

h =  hashlib.sha3_512(data)
print(h.hexdigest())