import socket
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    rand = random.uniform(1.2, 10.9)
    print("received message: %s" % str(data))
    print("addr %s",addr)
    sock.sendto(bytes(str(float(data)*rand),'utf-8'),addr)