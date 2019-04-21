#!/usr/bin/env python3


from socketServer.socketUnderlay import SocketUnderlay

import os
from os.path import join, getsize

def getFileListing():
    #file transfer
    #sending directory list
    dirList = list()
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd, topdown=True):
        del dirs[:]  # remove the sub directories.
        for file in files:
            dirList.append((file+" "+str(getsize(join(root, file)))))
            
    dirListString = '+.+.+'.join(dirList)
    print(dirListString)
    dirListBin = bytes(dirListString,'utf-8')
    return dirList, dirListBin

def main():
    #create binding of host with port
    print('Waiting for incoming connections...')

    s1 = SocketUnderlay()
    
    #listen for connection
    addr = s1.startListening()
    print(addr, "has connected to the server")
    cwdList, cwdListBin = getFileListing()
    s1.sendData(cwdListBin)
    
    #recv request for file
    fileReqBin = s1.recvData(1024)
    
    #convert binary data into str
    fileReqStr = fileReqBin.decode('utf-8')
    
    #remove size value from list
    dirListNames = list(x.split(" ")[0] for x in cwdList)

    #check if the file is present
    if fileReqStr in dirListNames:
        with open(fileReqStr, 'rb') as f:
            reqFileTrans = f.read()
        #send the binary data to client
        s1.sendData(reqFileTrans)
    #close connection
    s1.closeConn()




if __name__ == '__main__':
    main()
