import socket
import threading
import elgamal
import jsonDB

nickname = input("Nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client's key and public exponent
sKey = elgamal.keygen()
h = elgamal.public_exp(sKey)

jsonData = {"client": nickname,"publicKey": h}
jsonDB.write_json(jsonData)

waitingSignature = input("Please turn on two clients and then type y: ")

#connect to the server
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "NICK":

                client.send(nickname.encode('utf-8'))

            else:
                # Decryption
                cipherArray = message.split(" ")
                if(cipherArray[1] != nickname):
                    if(cipherArray[0] == "CHATMSG" and len(cipherArray) == 5):
                        c1 = int(cipherArray[2])
                        c2 = int(cipherArray[3])
                        signature = cipherArray[4]
                        sender = cipherArray[1]
                        plainmsg = f'{sender} > {elgamal.decrypt(c1,c2,sKey)}' 
                        print(plainmsg)
                    else:
                        print(message)
        except:
            print("ERROR")
            client.close()
            break

def write():

    while True:

        targetPubKey = jsonDB.getPublicKey(nickname)

        plainMessage = input("")

        c1,c2,signature = elgamal.encrypt_signed(plainMessage, targetPubKey)

        sendMessage = "CHATMSG" + " " + nickname + " " + str(c1) + " " + str(c2) + " " + str(signature)

        print(f'{nickname} > {plainMessage}')

        client.send(sendMessage.encode('utf-8'))


receive_thread  = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()