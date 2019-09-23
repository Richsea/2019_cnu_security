
MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')
        mode = input().lower()

        if mode in 'encrypt e decrypt d'.split():
            return mode

        else:
            print('The value you entered its invalid')

def getFileName():
    print("Enter your file name:")
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key(a-z)')
        key = input().lower()
        if(key.isalpha()):
            return key
        
def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    cryptoAl = 1
    
    if mode[0] == 'd':
        cryptoAl = -1
        outputFileName = 'decrypt.txt'
        
    translated = ''
    outputFile = open(outputFileName, 'w')
    
    inputFile = open(fileName, 'r')
    message = inputFile.read()
    
    keyBlock = []
    
    for i in range(len(key)):
        keyBlock.append((ord(key[i]) - 97) * cryptoAl)
    
    count = 0
    for symbol in message:
        translated += shift(symbol, keyBlock[count % len(keyBlock)])
        count += 1 
    
    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print('En(De)cryption complete')
    
def shift(symbol, key):
    asciiNum = ord(symbol)
    
    if asciiNum > 64 and asciiNum < 91:
        asciiNum = asciiNum + key
        if asciiNum <= 64:
            asciiNum = 91-(65-asciiNum)
            
        elif asciiNum >= 91:
            asciiNum = 65+(asciiNum - 91)
    
        return chr(asciiNum)
    elif asciiNum > 96 and asciiNum < 123:
        asciiNum = asciiNum + key
        if asciiNum <= 96:
            asciiNum = 123-(97-asciiNum)
            
        elif asciiNum >= 123:
            asciiNum = 97+(asciiNum - 123)
        
        return chr(asciiNum)
	
    else:
	    return chr(asciiNum)


mode = getMode()
key = getKey()
fileName = getFileName()
encrypt(mode, fileName, key)
