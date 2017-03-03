import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

print 'wating for connection'

connection, address = sock.accept()
print 'connected:', address

while True:
    data = connection.recv(1024)
    if data:
        print data
        connection.send(data.upper())
    else:
        connection.close()
        print 'connection closed. wating for connection'

        connection, address = sock.accept()
        print 'connected:', address

