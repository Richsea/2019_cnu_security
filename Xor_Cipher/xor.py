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

def getKey():
	key = 0
	while True:
		print('Enter the key')
		key = input()
		return key

def encrypt(mode, fileName, key):
	keyValue = ''

	outputFileName = 'encrypt.txt'
	if mode[0] == 'd':
		outputFileName = 'decrypt.txt'
	
	translated = ''
	outputFile = open(outputFileName, 'w')

	inputFile = open(fileName, 'r')
	message = inputFile.read()

	for i in range(len(message)//3):
	  	keyValue += key

	translated = str_xor(keyValue, message)
	outputFile.write(translated)
	outputFile.close()
	inputFile.close()
	print('En(De)cryption complete')

def str_xor(keyValue, message):
    data = ''
    for i in range(len(message)):
        data += chr(ord(str(message[i])) ^ ord(keyValue[i % len(keyValue)]))
    return data

mode = getMode()
key = getKey()
fileName = getFileName()
encrypt(mode, fileName, key)
		
