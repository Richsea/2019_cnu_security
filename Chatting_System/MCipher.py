from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

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
