import socket

def server_program():
    host = '127.0.0.1'
    port = 5462

    key = 'thisisbadkeyokeythisisbadkeyokey'
    iv = 'ivisinitialvetor'

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    conn.send(key.encode())
    print(conn.recv(1024).decode())
    conn.send(iv.encode())
    print(conn.recv(1024).decode())

    print("Connection from: " + str(address))

    while True:
        rdata = conn.recv(1024)
        if not rdata:
            break
        data = rdata.decode()
        print("Recieved from user2 : " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
