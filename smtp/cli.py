import socket, ssl, base64

endmsg = '\r\n.\r\n'
user = '*****'
password = '*****'
mailTo = raw_input("To: ")
subject = raw_input("Subject: ")
message = raw_input("Message: ")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('smtp.gmail.com', 587))
recv = socket.recv(1024)
print recv
if recv[:3] != '220':
    print 'did not get code 220'

# Send command HELO
socket.send('EHLO 127.0.1.1\r\n')
recv = socket.recv(1024)
print recv
if recv[:3] != '250':
    print 'did not get code 250'

# Send STARTTLS command to server and print server response
socket.send("STARTTLS\r\n")
recv = socket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

ssl_socket = ssl.wrap_socket(socket)

# Send command HELO
ssl_socket.send('EHLO 127.0.1.1\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '250':
    print 'did not get code 250'

# Send command AUTH LOGIN
ssl_socket.send('AUTH LOGIN\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '334':
    print '334 reply not received from server.'

ssl_socket.send(base64.b64encode(user)+'\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '334':
    print '334 reply not received from server.'

ssl_socket.send(base64.b64encode(password)+'\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '235':
    print '235 reply not received from server.'

# Send command MAIL FROM
ssl_socket.send('MAIL FROM:<' + user + '>\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '250':
    print 'did not get code 250'

# Send command RCPT TO
ssl_socket.send('RCPT TO:<' + mailTo + '>\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '250':
    print 'did not get code 250'

# Send command DATA
ssl_socket.send('DATA\r\n')
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '354':
    print 'did not get code 250'

# Send message
ssl_socket.send("Subject: " + subject + "\r\n\r\n" + message + "\r\n.\r\n")
ssl_socket.send(endmsg)
recv = ssl_socket.recv(1024)
print recv
if recv[:3] != '250':
    print 'did not get code 250'

ssl_socket.close()
