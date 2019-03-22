from socket import *
from time import time

serverAddress = ('', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for messageCounter in range(1, 10):
    now = time()

    message = 'Ping ' + str(messageCounter) + ' ' + str(now)
    print message

    try:
        clientSocket.sendto(message, serverAddress)
        modifiedMessage, addr = clientSocket.recvfrom(1024)
        print modifiedMessage

        rtt_time = time() - now
        print 'RTT time: ', rtt_time
    except timeout as err:
        print 'Request timed out'

clientSocket.close()
