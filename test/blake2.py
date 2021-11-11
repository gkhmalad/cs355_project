import hashlib

h = hashlib.blake2b(key=b'01011000101010110111', digest_size=64)

h.update(b"Hello World")
print(h.hexdigest())