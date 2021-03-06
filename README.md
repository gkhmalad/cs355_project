# cs355_project
CS355 Cryptography Project

## Stack
- Python
- hashlib, hmac, os, binascii

## Protocol
- Diffie-Hellman Public Key Exchange
- El Gamal Encryption
- HMAC Signatures
- SHA3-512 hashing
- Simple TCP Communication Platform
- Extremely Simple JSON Database

## HOWTO
There are different ways to run the code. There are three different El Gamal implementations in this repository. This is because transforming different types of input (string, hex, int) was causing major bugs. All of these are implemented separately so the bugs do not happen.
### elgamalChat.py
This implementation concerns the actual TCP communication platform. To run this we have to interact with two other files `client.py` and `server.py`. To run the server please strictly follow these instructions!
- Run `server.py`. It should prompt "Server is listening..." in the terminal
- Open two other terminal windows and run `client.py` in both. Choose the nicknames BUT do not type y until both nicknames have been typed. This is going to cause a crash because the simple JSON database for public keys will not be ready until both nicknames are typed.
- Do not run more than 2 clients as they will not be able to decrypt the messages and will just get prompted by message tampering.
- The algorithm for picking "the other clients" public key works by picking the one that is not yours. It is very rudimentary and can only handle 2 clients.
- If everything is done properly, the two clients can chat between each other while seeing plaintext, as encryption and decryption are running in the background.

### elgamalHomomorphic.py
This implementation demonstrates the homomorphic division for El Gamal with simple integers. It has been altered in the decryption algorithm to decrypt integers instead of strings to avoid bugs. Just run the file to generate answers. The main function can be altered to see cryptographic keys, signatures, ciphertexts and everything else.

### elgamalDigestComparison.py
This implementation concerns the main objective of the project. It compares the digests of two password files that are generated by `password_file_generator.py`. For demonstration and testing purposes, generate two separate password files and try using the same and different ones to test the correctness. Like in the previous example, anything can be added to the main function for more clarity and testing.