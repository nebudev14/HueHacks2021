import socket

while True:
    s = socket.socket()
    host = '' # ip of server
    port = 12345 
    s.connect((host, port))
    message = s.recv(1024)
    print(message.decode("utf-8"))