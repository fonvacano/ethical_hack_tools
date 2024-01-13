from socket import *

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
connection, addr = serverSocket.accept()
print('Thank you for connecting to me ' + str(addr))
message = connection.recv(1024).decode()
print(message)
command = ''
while command != 'exit':
    command = input('Enter command:')
    connection.send(command.encode())
    response = connection.recv(1024).decode()
    print(response)
connection.shutdown(SHUT_RDWR)
connection.close()

