from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
import hashlib

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s [:-ord(s[len(s) - 1:])]

priKey = RSA.generate(1024) # private key 생성
pubKey = priKey.publickey() # public key에서 private key 생성

def setAES(key, iv):
    #TODO SET AES
    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv.encode("UTF-8"))

    return cipher

def AES_Encrypt(cipher, data):
    #TODO DATA ENCRYPT
    message = pad(data)

    message = cipher.encrypt(message.encode("UTF-8"))  # 결과는 byte 코드
    message = base64.b64encode(message)

    return message

def AES_Decrypt(cipher, data):
    #TODO DATA DECRYPT
    message = base64.b64decode(data)    # byte코드 나옴
    message = cipher.decrypt(message)

    message = unpad(message).decode("UTF-8")

    return message

###################################################################
# RSA encryption function
###################################################################

def createPEM(pri_filename, pub_filename):
    priFile = open("./" + pri_filename, "wb+")
    priFile.write(priKey.exportKey('PEM'))
    priFile.close()

    pubFile = open("./" + pub_filename, "wb+")
    pubFile.write(pubKey.exportKey('PEM'))
    pubFile.close()

def readPEM(filename):
    file = open(filename, "r")
    priKey = RSA.importKey(file.read()) # return RSA key object
    file.close()
    return priKey

def RSAEncrypt(pubKey, data):
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypt = encryptor.encrypt(data.encode("UTF-8"))
    return encrypt

def RSADecrypt(pubKey, data):
    decryptor = PKCS1_OAEP.new(pubKey)
    decrypt = decryptor.decrypt(data)
    return decrypt.decode("UTF-8")

#################################################
# E[M + Hash(M)]
#################################################

def sha256(data):
    hashData = hashlib.sha256(data.encode()).hexdigest()
    return hashData

def makeHashBlock(data, priKey):
    hashData = sign(priKey, data)
    hashBlock = '{0:04x}'.format(len(data)) + data + '{0:04x}'.format(len(hashData)) + hashData

    return hashBlock

def separateHashBlock(hashBlock):
    data_size = int(hashBlock[:4], 16)
    realData = hashBlock[4 : data_size+4]

    hash_data_size = int(hashBlock[data_size+4:len(hashBlock)], 16)
    hashData = hashBlock[data_size+8 : hash_data_size]

    return realData, hashData

'''
def integrityCheck(data, hashData):
    getHashData = sha256(data)

    return getHashData == hashData
'''

###################################################
# Electronic signature
###################################################

def sign(priKey, hashData):
    hasher = SHA256.new(hashData.encode('UTF-8'))
    hasher = hasher.hexdigest()
    
    signer = PKCS1_v1_5.new(readPEM(priKey))
    signature = signer.sign(hasher)

    print(signature)

    return signature

def verify(pubKey, message, signData):  # message는 message를 복호화 해서 hash화 한 값
    verifier = PKCS1_v1_5.new(readPEM(pubKey))
    hasher = SHA256.new(message.encode())
    if verifier.verify(hasher, signData):
        print("it is user message")
    else:
        print("no!")
        return False

    return True