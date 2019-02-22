import socket, ssl

endmsg = '\r\n.\r\n'
user = '*****'
password = '******'

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(socket)
ssl_socket.connect(('pop.gmail.com', 995))
recv = ssl_socket.recv(1024)
print recv

ssl_socket.send('USER ' + user + '\r\n')
recv = ssl_socket.recv(1024)
print recv

ssl_socket.send('PASS ' + password + '\r\n')
recv = ssl_socket.recv(1024)
print recv

ssl_socket.send('TOP 1 10\r\n')
recv = ssl_socket.recv(1024)
print recv

ssl_socket.send('QUIT\r\n')
recv = ssl_socket.recv(1024)
print recv
