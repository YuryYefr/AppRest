"""This is just echo to broadcast through network"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
clients = {}
addresses = {}
HOST = ''
PORT = 45000    # Don't forget to pass exact to client
SERVER_ID = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(SERVER_ID)


def receiving_connections():
    """thread for incoming"""
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} has connected")
        addresses[client] = client_address
        Thread(target=client_handling, args=(client,)).start()


def client_handling(client):
    """transmitting to client"""
    name = client.recv(1024).decode('utf8')
    clients[client] = name
    while True:
        msg = client.recv(1024)
        if msg != bytes('', 'utf8'):
            echo(msg)
        else:
            client.send(bytes('', 'utf8'))
            client.close()
            del clients[client]
            print(name + ' has disconnected')
            break


def echo(msg, client_name=''):
    """echoing to network"""
    for sock in clients:
        sock.send(bytes(client_name, 'utf8') + msg)


if __name__ == "__main__":
    SERVER.listen(5)  # 5 connections at one time
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=receiving_connections())
    ACCEPT_THREAD.start()  # Starting loop.
    ACCEPT_THREAD.join()   # Waiting for each thread to complete
    SERVER.close()         # Shutdowns receiving
