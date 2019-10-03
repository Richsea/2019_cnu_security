import socket
import MCipher

def server_program():
    host = '127.0.0.1'
    port = 5462

    key = 'thisisbadkeyokeythisisbadkeyokey'
    iv = 'ivisinitialvetor'

    server_socket = socket.socket()		# 소켓 생성
    server_socket.bind((host, port))	# 소켓 주소 정보할당

    server_socket.listen(2)				# 연결 수신 대기
    conn, address = server_socket.accept() #연결 수락	return 는 (conn, address) pair. conn : new socket object usable to send and receive data on the connectoin
    conn.send(key.encode())				# 데이터 전송
    print(conn.recv(1024).decode())
    conn.send(iv.encode())

    print(conn.recv(1024).decode())

    print("Connection from: " + str(address))

    while True:
		# 수신받은 데이터 정리
        rdata = conn.recv(1024)	#byte 데이터

        if not rdata:
            break
        cipher = MCipher.setAES(key, iv)
        data = rdata.decode('UTF-8')
        data = MCipher.AES_Decrypt(cipher, data)
        print("Recieved from user2 : " + str(data))
        data = input(' -> ')
        cipher = MCipher.setAES(key, iv)
        conn.send(MCipher.AES_Encrypt(cipher, data))

    conn.close()

if __name__ == '__main__':
    server_program()
