"""This is just echo to broadcast through network"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class EchoServer:
    # retrieve_data = []
    clients = {}
    addresses = {}
    HOST = ''
    PORT = 35000  # Don't forget to pass exact to client
    SERVER_ID = (HOST, PORT)
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(SERVER_ID)

    def receiving_connections(self):
        """thread for incoming"""
        while True:
            client, client_address = self.SERVER.accept()
            print(f"{client_address} has connected")
            # for i in self.retrieve_data:
            #     print(i)
            #     client.send(bytes(i, 'utf8'))
            #     time.sleep(1)
            self.addresses[client] = client_address
            Thread(target=self.client_handling, args=(client,)).start()

    def client_handling(self, client):
        """transmitting to client"""
        name = client.recv(1024).decode('utf8')
        self.clients[client] = name
        while True:
            msg = client.recv(1024)
            if msg != bytes('', 'utf8'):
                # self.retrieve_data.append(name)
                self.echo(msg)
                # print(self.retrieve_data)
            else:
                client.send(bytes('', 'utf8'))
                client.close()
                del self.clients[client]
                print(name + ' has disconnected')
                break

    def echo(self, msg, client_name=''):
        """echoing to network"""
        for sock in self.clients:
            sock.send(bytes(client_name, 'utf8') + msg)


if __name__ == "__main__":
    EchoServer.SERVER.listen(5)  # 5 connections at one time
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=EchoServer().receiving_connections())
    ACCEPT_THREAD.start()  # Starting loop.
    ACCEPT_THREAD.join()  # Waiting for each thread to complete
    EchoServer.SERVER.close()  # Shutdowns receiving
