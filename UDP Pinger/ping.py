#in ping.py the client connects to the server and sends a ping message to the server, the server then responds with a
#pong message.

#importing some needed modules
import argparse
import socket
from socket import socket as Socket
import sys
import time

def main():

    #adding some required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--server-port', '-p', default=2081, type=int, help='server_port to use')
    parser.add_argument('--run-server', '-s', action='store_true', help='run a ping server')
    parser.add_argument('server_address', default='localhost', help='server to ping, no effect if running as a server.')
    args = parser.parse_known_args()

    if args.run_server:
        return run_server(args.server_port)
    else:
        return run_client(args.server_address, args.server_port)

#start the server
def run_server(server_port):
    """Run the UDP pinger server"""
    #server socket
    with Socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', server_port))
        #accept ping requests
        print("Ping server ready on port", server_port)
        while True:
            _, client_address = server_socket.recvfrom(1024)
            server_socket.sendto("".encode(), client_address)
    return 0

#runs the client
def run_client(server_address, server_port):
    """"Ping a UDP pinger server running at the given address"""

    with Socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        client_socket.settimeout(1.0)

        #Send 10 UPD packets to the server
        print("pinging", str(server_address), "on port", server_port)
        for i in range(10):
            #send packet to server
            client_socket.sendto("".encode(), (server_address, server_port))
            #recieve packets/print results
            try:
                timer_start = time.time()
                _, _ = client_socket.recvfrom(1024)
                timer_stop = time.time()
            except socket.timeout:
                print("packet lost")

            else:
                print("Round trip time: {:.ef}ms".format((timer_stop - timer_start)*1000))

    return 0

if __name__ == "__main__":
    sys.exit(main())