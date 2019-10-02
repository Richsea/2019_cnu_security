import socket

def client_program():
    host = '127.0.0.1'
    port = 5462

    keyRecive = False
    client_socket = socekt.socket()
    client_socket.connect((host, port))

    if(keyRecive == False):
        key = client_socket.recv(1024).decode()
        print('key : ' + key)
        client_socket.send('key exchange Success'.encode())
        iv = client_socekt.recv(1024).decode()
        print('iv : ' + iv)
        client_socket.send('iv exchange Success'.encode())
        keyRecive = True

    if(keyRecive):
        message = input(" -> ")
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())
            data = client_socekt.recv(1024)
            data = data.decode()
            print('Received from userl : ' + data)

            message = input(" -> ")
    client_socket.close()

if __name__ == '__main__':
    client_program()
