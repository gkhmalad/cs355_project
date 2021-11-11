import hashlib

h = hashlib.sha3_256(b"Nobody inspects the spammish repetition")
m = hashlib.sha3_256(b"Nobody inspects the spammish repetition")

print(h.hexdigest())
print(m.hexdigest())


print('Hello')