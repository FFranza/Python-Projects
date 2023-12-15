from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os

def encrypt(dataFile, publickeyFile):
    with open(dataFile, 'rb') as f: # Reads content of file
        data = f.read()

    data = bytes(data) # Converts data into bytes

    with open(publickeyFile, 'rb') as f:
        publicKey = f.read()
    
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []

    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print(f"Encrypted file saved to: {encryptedFile}")

def decrypt(dataFile, publickeyFile):
    with open(privateKeyFile, 'rb') as f: # Reads content of file
        privateKey = f.read()
        key = RSA.import_key(privateKey)

    with open(dataFile, 'rb') as f:
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]
    
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb' ) as f:
        f.write(data)

print("Encrypt or Decrypt a File?")
user_response = input("")
if user_response == "Encrypt":
    print("Please type the exact file name")
    data = input("")
    publicKeyFile = 'public.pem'
    encrypt( data, publicKeyFile)
elif user_response == "Decrypt":
    print("Please type the exact file name")
    decryptFile = input("")
    privateKeyFile = 'private.pem'
    decrypt(decryptFile, privateKeyFile)
else:
    print("Exiting Script")
    exit