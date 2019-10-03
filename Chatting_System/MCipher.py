from Crypto.Cipher import AES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s [:-ord(s[len(s) - 1:])]

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

