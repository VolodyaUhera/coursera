import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

IP = "127.0.0.1"
Port = 5005

sock.bind((IP, Port))

while True:
    data, addr = sock.recvfrom(1024)
    print ("received message: ", data)