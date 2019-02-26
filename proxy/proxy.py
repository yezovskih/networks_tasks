from socket import *

TCP_IP = 'localhost'
TCP_PORT = 8888
server_address = (TCP_IP, TCP_PORT)

# Create tcp server
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(server_address)
print 'starting up on %s port %s' % server_address
tcpServerSocket.listen(1)

while True:
    print 'Proxy Server is ready...'
    tcpClientSocket, addr = tcpServerSocket.accept()
    print 'Connection established with:', addr
    # Receive the data in chunks and retransmit it
    message = tcpClientSocket.recv(1024)
    print message
    if not message: break

    filename = message.split()[1].partition("/")[2]
    print 'Filename: ', filename
    fileExist = False
    try:
        # Check file in cache
        f = open("./proxy/.cache/" + filename, "r")
        data = f.readlines()
        fileExist = True
        # Send to client
        tcpClientSocket.send("HTTP/1.0 200 OK\r\n")
        tcpClientSocket.send("Content-Type:text/html\r\n")
        for line in data:
            tcpClientSocket.send(line)
    except IOError:
        if not fileExist:
            c = socket(AF_INET, SOCK_STREAM)
            try:
                hostname = filename.replace("www.","",1)
                port = 80
                c.connect((hostname, port))
                print 'connected to %s port %s' % (hostname, port)

                fileobj = c.makefile('r', 0)
                fileobj.write("GET "+"http://" + filename + "HTTP/1.0\n\n")

                # Read the response into buffer
                buffr = fileobj.readlines()
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the
                # corresponding file in the cache
                tmpFile = open("./proxy/.cache/" + filename,"wb")
                for data in buffr:
                    tmpFile.write(data)
                    tcpClientSocket.send(data)
            except Exception as err:
                print err
        else:
            # Send 404 Not Found
            tcpClientSocket.send("HTTP/1.0 404 NOT FOUND\r\n")
            print '404 NOT FOUND'
    finally:
        tcpClientSocket.close()

tcpServerSocket.close()
