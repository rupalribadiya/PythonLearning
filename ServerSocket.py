import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(3) # How many client you want to connect

print('Connected Successfully!')
print('Waiting for a Connection..')

while True:
    c, addr = s.accept()

    name = c.recv(1024).decode();
    print('Client connected ', addr, name)

    c.send(bytes('Welcome {}'.format(name), 'utf-8'))
    c.close()