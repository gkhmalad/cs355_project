import hashlib

h = hashlib.sha3_256(b"Nobody inspects the spammish repetition")

integerDigest = int(h.hexdigest(), 16)

print(h.hexdigest())
print(hex(integerDigest)[2:])
print(h.hexdigest() == hex(integerDigest)[2:])

print('Hello')