# cs355_project
CS355 Cryptography Project

## HOWTO
There are different ways to run the code. There are three different El Gamal implementations in this repository. This is because transforming different types of input (string, hex, int) was causing major bugs. All of these are implemented separately so the bugs do not happen.
### elgamalChat.py
This implementation concerns the actual TCP communication platform. To run this we have to interact with two other files `client.py` and `server.py`.