import socket
import threading
import elgamal

nickname = input("Nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
                print(message)
        except:
            print("ERROR")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        # Encryption
        client.send(message.encode('utf-8'))

receive_thread  = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()