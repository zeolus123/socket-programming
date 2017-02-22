#modules
from socket import *
import time

#server variables
serverName = 'localhost'
serverPort = 8000

#creating socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#sending message 10 times and finding round trip time
for x in range(0, 10):
    message = 'Ping!'
    print(message)
    send_time = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # recieving message
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    rec_time = time.time()
    print(modifiedMessage.decode())
    print(rec_time - send_time)

#closing socket
clientSocket.close()