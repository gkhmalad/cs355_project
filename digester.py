import hashlib

def file_digest(fpath):

    # rb mode reads in binary, omits \n and such
    with open(fpath, 'rb') as file:
        data = file.read()

    h =  hashlib.sha3_512(data)

    return h.hexdigest()