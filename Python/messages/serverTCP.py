import socket

sock = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)

IP = "127.0.0.1"
PORT = 5005

BUFFER_SIZE = 1024

sock.bind((IP, PORT))

sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    conn.send(data)
    print ("received data: ", data)

conn.close()
