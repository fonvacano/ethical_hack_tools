import sys, socket

size = 1024


def send_smtp(smtp_server, port, sender, receiver, message_payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((smtp_server, port))
        print(s.recv(size).decode())
        s.send(('HELO' + sender.split('@')[1]).encode() + b'\n')
        print(s.recv(size).decode())
        # отправка адреса отправителя
        s.send(b'MAIL FROM:<' + sender.encode() + b'>\n')
        print(s.recv(size).decode())
        # кому аддресовано
        s.send(b'RCPT TO:<' + receiver.encode() + b'>\n')
        print(s.recv(size).decode())
        # отправляем данные
        s.send(message_payload.encode() + b'\n')
        s.send(b'\r\n.\r\n')
        print(s.recv(size).decode())
        s.send(b'QUIT\n')


def main(args):
    smtp_addr = args[1]
    port = args[2]
    sender = args[3]
    receiver = args[4]
    data = args[5]
    send_smtp(smtp_addr, port, sender, receiver, data)
    print('message was successfully sent')


if __name__ == '__main__':
    main(sys.argv)
