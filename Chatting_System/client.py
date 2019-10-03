import socket
import MCipher

def client_program():
    host = '127.0.0.1'
    port = 5462

    keyRecive = False
    client_socket = socket.socket()
    client_socket.connect((host, port))

    if(keyRecive == False):
        key = client_socket.recv(1024).decode()
        print('key : ' + key)
        client_socket.send('key exchange Success'.encode())
        iv = client_socket.recv(1024).decode()
        print('iv : ' + iv)
        client_socket.send('iv exchange Success'.encode())
        keyRecive = True

    if(keyRecive):
        message = input(" -> ")

        while message.lower().strip() != 'bye':
            cipher = MCipher.setAES(key, iv)
            client_socket.send(MCipher.AES_Encrypt(cipher, message))
            data = client_socket.recv(1024)
            cipher = MCipher.setAES(key, iv)
            data = MCipher.AES_Decrypt(cipher, data.decode("UTF-8"))
            print("Received from user1 : " + data)
            
            message = input(" -> ")
    client_socket.close()

if __name__ == '__main__':
    client_program()
