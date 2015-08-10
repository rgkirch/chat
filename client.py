import socket
import json

port = 50010
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
host = socket.gethostname()
s.connect( (host, port) )

obj = {}
obj['message'] = "hello"

s.sendall( json.dumps( obj ) )
#data = s.recv( 1024 )
s.close()
#print repr(data)
