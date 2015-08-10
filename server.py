import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
sock.bind( ("", 50010) )
sock.listen( 1 )
while 1:
    connection, address = sock.accept()
    data = json.loads( connection.recv(1024) )
    print data['message']
    #connection.sendall( pickle.dumps(data) )
    connection.close()
#print socket.gethostname()
#print socket.gethostbyname(socket.gethostname())

