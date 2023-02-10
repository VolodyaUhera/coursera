import time, socket, sys

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char == " "):
         result += " "
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) - s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char == " "):
         result += " "
      else:
         result += chr((ord(char) - s - 97) % 26 + 97)
    return result

s = 4
print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
while True:
   message = soc.recv(1024)
   message = decrypt(message.decode(), s)
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "[bye]":
      message = "Leaving the Chat room"
      soc.send(encrypt(message, s).encode())
      print("\n")
      break
   soc.send(encrypt(message, s).encode())
