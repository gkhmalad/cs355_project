import threading
import socket

host = '127.0.0.1' #localhost
port = 55555

#create server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the server
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Message sending
def broadcast(message):
    for client in clients:
        client.send(message)

# Handles connections of each client
def handle(client):
    while True:
        # Try sending message. If error, remove
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} timed out.'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Accepts conenctions
def receive():
    while True:
        # Accept Client
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask for nickname, keep in list
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} has connected!".encode('utf-8'))
        client.send('Connected to the chatroom!'.encode('utf-8'))

        # Start thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()