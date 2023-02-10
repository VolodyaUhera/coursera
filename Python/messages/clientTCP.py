import socket

IP = "127.0.0.1"
PORT = 5005

BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.connect((IP, PORT))

sock.send(input().encode())

data = sock.recv(BUFFER_SIZE)

sock.close()

print ("recieved data: ", data)

