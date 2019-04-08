#!/usr/bin/env python3

import os
import argparse
import binascii
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


#to read file as binary
def readfile_binary(file):
    with open(file, 'rb') as f:
        content = f.read()
    return content


#to write file in binary
def writefile_binary(file, content):
    with open(file, 'wb') as f:
        f.write(content)


def encrypt_aes_128_cbc(content, key, iv):
    
    #padding for block ciphers
    padder = padding.PKCS7(128).padder()
    padded_content = padder.update(content)

    backend = default_backend()
    
   #create cipher profile
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=backend)
    
    #encrypt message
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_content) + encryptor.finalize()
#    print(type(ciphertext))
 #   print(str(ciphertext))
    #key = os.urandom(16)
    #iv = os.urandom(16)
    
    return ciphertext


#main method to accept cmd line arguments and generate output
def main():
    parser = argparse.ArgumentParser(description = 'Method to perform cryptographic operations')
    parser.add_argument('-in', dest = 'input', required = True, help = 'input filename')
    parser.add_argument('-out', dest = 'output', required = True, help = 'output filename')
    parser.add_argument('-K', dest = 'key', required = True, help = 'Key to be used for encryption/decryption')
    parser.add_argument('-iv', dest = 'iv', required = True, help = 'Initialization vector input')
    parser.add_argument('--encrypt', required = True, help = 'encryption operation', action = 'store_true')

    args = parser.parse_args()
    backend = default_backend()

    if args.encrypt:
        input_key = binascii.unhexlify(args.key)
        input_iv = binascii.unhexlify(args.iv)
        
        #read file input
        content = readfile_binary(args.input)
        
        #call method to encryption
        ciphertext = encrypt_aes_128_cbc(content, input_key, input_iv)
        writefile_binary(args.output, ciphertext)
    
if __name__ == "__main__":
    main()
#    input_content = readfile_binary(



 
#       decryptor = cipher.decryptor()
#    decryptor.update(ct) + decryptor.finalize()

