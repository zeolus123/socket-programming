#need a module
from socket import *

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server ready to recieve")

while True:
    modifiedMessage, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = 'Pong!'
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)