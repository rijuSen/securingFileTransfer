#!/usr/bin/env python3

class SocketUnderlay:
    def __init__(self):
        import socket
        self.host = socket.gethostname()
        self.port = 7777
        self.s = socket.socket()
        self.s.bind((self.host,self.port))

    def startListening(self):
        #Waiting for incoming connections...
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        return self.addr 


    def sendData(self,binData):
        self.conn.send(binData)

    def recvData(self,dataSize):
        recvData = self.conn.recv(dataSize)
        return recvData

    def closeConn(self):
        self.s.close()
