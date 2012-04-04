from gevent import Greenlet
from gevent.socket import *

def echo(socket, addr):
    print '...connected from:', addr
    fileobj = socket.makefile()
    while True:
        line = fileobj.readline()
        if not line: break
        fileobj.write("echo: "+line)
        fileobj.flush()

serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind( ('localhost',8080) )
serversock.listen(2)

while 1:
     print 'waiting for connection...'
     clientsock, addr = serversock.accept()
     Greenlet(echo, clientsock, addr).start()

