# socket-programming
<h7>For CSCI3171(Network Computing) assignment 2.</h7>

<h3>UDP Pinger</h3>
This is programming assigment 2 from the text book. It's composed to to python scripts, UDPPingerClient and
UDPPingerServer. Once the Server script is running it waits for the client to send it packets. The client script then
sends 10 messages, waits for the return message and calculates the round trip time.
To run the ping application on one machine I just ran UDPPingerServer.py from the command line and then subsequently
ran UDPPingerClient.py from my PyCharm IDE, running it from another command line instance would also suffice.