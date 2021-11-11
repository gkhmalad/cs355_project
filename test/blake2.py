import hashlib

h = hashlib.blake2b(key=b'Gugi')

h.update(b"Hello World")
print(h.hexdigest())