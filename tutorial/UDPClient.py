from socket import *

#server variables
serverName = 'localhost'
serverPort = 8000

#creating the client socket0
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence')

#sending the message
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#printing the modified decoded message
print(modifiedMessage.decode())

#closing socket
clientSocket.close()