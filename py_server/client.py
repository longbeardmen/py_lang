import socket
import time
from random import randint

sock = socket.socket()
sock.connect(('localhost', 9090))

for i in xrange(1,10):
    sock.send(str(randint(1,10)))
    data = sock.recv(1024)
    print data
    time.sleep(1)

sock.close()

