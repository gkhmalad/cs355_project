import hashlib
import password_file_generator

def file_gen():
    password_file_generator.password_gen()


# Generates a digest of the passwords file
def file_digest(fpath):

    # rb mode reads in binary, omits \n and such
    with open(fpath, 'rb') as file:
        data = file.read()

    h =  hashlib.sha3_512(data)

    return h.hexdigest()