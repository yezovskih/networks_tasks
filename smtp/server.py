import socket, ssl
from smtp.mail import Mail

endmsg = "\r\n.\r\n"
mail = Mail()

while True:
    mail.create()

    # Создаем сокет ssl socket и устанавливаем TCP-соединение с почтовым сервером
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context()
    ssl_socket = context.wrap_socket(socket, server_side=True)
    ssl_socket.connect(("smtp.gmail.com", 587))
    recv = ssl_socket.recv(1024)
    print recv
    if recv[:3] != '220':
         print 'код 220 от сервера не получен.'

    # Отправляем команду HELO и выводим ответ сервера.
    ssl_socket.send('HELO\r\n')
    recv1 = ssl_socket.recv(1024)
    print recv1
    if recv1[:3] != '250':
        print 'код 250 от сервера не получен.'

    # Отправляем команду MAIL FROM и выводим ответ сервера. # Начало вставки
    ssl_socket.send('MAIL FROM: <' + mail.mailFrom + '>')
    recv2 = ssl_socket.recv(1024)
    print recv2
    if recv2[:3] != '250':
        print 'код 250 от сервера не получен.'

    # Отправляем команду RCPT TO и выводим ответ сервера.
    ssl_socket.send('RCPT TO: <' + mail.mailTo + '>')
    recv3 = ssl_socket.recv(1024)
    print recv3
    if recv3[:3] != '250':
        print 'код 250 от сервера не получен.'

    # Отправляем команду DATA и выводим ответ сервера.
    ssl_socket.send('DATA')
    recv4 = ssl_socket.recv(1024)
    print recv4
    if recv4[:3] != '354':
        print 'код 354 от сервера не получен.'

    # Отправляем данные сообщения.
    ssl_socket.send(mail.message)
    ssl_socket.send(endmsg)
    recv5 = ssl_socket.recv(1024)
    print recv5
    if recv5[:3] != '250':
        print 'код 250 от сервера не получен.'

    # Отправляем команду QUIT и получаем ответ сервера.
    ssl_socket.send('QUIT')
    recv6 = ssl_socket.recv(1024)
    print recv6
    if recv6[:3] != '221':
        print 'код 221 от сервера не получен.'
