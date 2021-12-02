# cs355_project
CS355 Cryptography Project

## HOWTO
There are different ways to run the code. There are three different El Gamal implementations in this repository. This is because transforming different types of input (string, hex, int) was causing major bugs. All of these are implemented separately so the bugs do not happen.
### elgamalChat.py
This implementation concerns the actual TCP communication platform. To run this we have to interact with two other files `client.py` and `server.py`. To run the server please strictly follow these instructions!
- Run `server.py`. It should prompt "Server is listening..." in the terminal
- Open two other terminal windows and run `client.py` in both. Choose the nicknames BUT do not type y until both nicknames have been typed. This is going to cause a crash because the simple JSON database for public keys will not be ready until both nicknames are typed.
- Do not run more than 2 clients as they will not be able to decrypt the messages and will just get prompted by message tampering.
- The algorithm for picking "the other clients" public key works by picking the one that is not yours. It is very rudimentary and can only handle 2 clients.
- If everything is done properly, the two clients can chat between each other while seeing plaintext, as encryption and decryption are running in the background.