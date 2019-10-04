from Crypto.Cipher import AES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)  
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def getMode():
	while True:
		print('Enter either "encrypt" or "e" or "decrypt" or "d".')
		mode = input().lower()
		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
		    	print('The value you entered its invalid')

def getFileName():
	print('Enter your file name:')
	return input()

def crypto(mode, fileName):
	keyValue = ''
	iv = 'asefasdfefsdsdfe'
	key = 'thisisbadkeyokey'
	outputFileName = ''
	if mode[0] == 'e':
		outputFileName = 'encrypt.txt'
	elif mode [0] == 'd':
		outputFileName = 'decrypt.txt'
	
	translated = ''
	outputFile = open(outputFileName, 'w')
	
	inputFile = open(fileName, 'r')
	message = inputFile.read()

	iv = iv.encode("UTF-8")
	key = key.encode("UTF-8")
	
	if mode[0] == 'e':
		message = pad(message)
		
		cipher = AES.new(key, AES.MODE_CBC, iv)
		
		message = cipher.encrypt(message.encode('UTF-8'))
		message = base64.b64encode(message)
		
		message = message.decode('UTF-8')
		translated = message
		
	elif mode[0] == 'd':
		message = message.encode('UTF-8')
		message = base64.b64decode(message)
		
		cipher = AES.new(key, AES.MODE_CBC, iv)
		message = cipher.decrypt(message)
				
		message = unpad(message)
		message = message.decode('UTF-8')
		translated = message
	
	outputFile.write(str(translated))
	outputFile.close()
	inputFile.close()
	print('En(De)cryption complete')

mode = getMode()
fileName = getFileName()
crypto(mode, fileName)
		
