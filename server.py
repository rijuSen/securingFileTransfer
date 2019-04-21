#!/usr/bin/env python3


import socket

s = socket.socket()

host = socket.gethostname()

port = 7777

s.bind((host,port))
s.listen(1)
print('Waiting for incoming connections...')
conn, addr = s.accept()
print(addr, "has connected to the server")


#file transfer

#sending directory list

dirList = list()

import os
from os.path import join, getsize

cwd = os.getcwd()

for root, dirs, files in os.walk(cwd, topdown=True):
    del dirs[:]  # remove the sub directories.
    for file in files:
        dirList.append((file+" "+str(getsize(join(root, file)))))

dirListString = '+.+.+'.join(dirList)

print(dirListString)

dirListBin = bytes(dirListString,'utf-8')
conn.send(dirListBin)

#receive file request
fileReqBin = conn.recv(1024)
fileReqStr = fileReqBin.decode('utf-8')

print(fileReqStr)

#remove size value from list
dirListNames = list(x.split(" ")[0] for x in dirList)

#check if the file is present
if fileReqStr in dirListNames:
    with open(fileReqStr, 'rb') as f:
        reqFileTrans = f.read()

    conn.send(reqFileTrans)
s.close()
