def getMode():
	while True:
		print('Enter either "encrypt" or "e" or "decrypt" or "d".')
		mode = input().lower()
		if mode in 'decrypt d'.split():
			return mode
		else:
		    	print('The value you entered its invalid')

def getFileName():
	print('Enter your file name:')
	return input()

def encrypt(mode, fileName, size):
    outputFileName = 'decrypt.txt'
    
    translated = ''
    outputFile = open(outputFileName, 'w')
    outputFile = open(outputFileName, 'a')

    inputFile = open(fileName, 'r')
    message = inputFile.read()

    for i in range(0, 26):
        key = ''
        key += chr(97+i)
        
        for j in range(0, 26):
            key += chr(97+j)

            for k in range(0, 26):
                key += chr(97+k)
                
                keyValue=''
                for l in range(len(message) // size):
                    keyValue += key

                translated = str_xor(keyValue, message)
                print(translated)
                outputFile.write(translated + '\n')
                key = key[:-1]
            key = key[:-1]

    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')

def str_xor(keyValue, message):
    data = ''
    for i in range(len(message)):
        data += chr(ord(str(message[i])) ^ ord(keyValue[i % len(keyValue)]))
    return data


mode = getMode()
fileName = getFileName()
encrypt(mode, fileName, 3)
		
