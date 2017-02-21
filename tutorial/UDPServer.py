from socket import *

#server variables
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_DGRAM)

#binding server socket to port number given
serverSocket.bind(('', serverPort))
print("The server is ready to recieve")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)