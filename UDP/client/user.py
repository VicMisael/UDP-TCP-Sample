import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

message = float(input("Enter any number: "))
print("value of val2: ", message)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % message)



sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(10.0)
sock.sendto(bytes(str(message), 'utf-8'), (UDP_IP, UDP_PORT))


try:
    data, server = sock.recvfrom(1024)
    print(f'{data}')
except socket.timeout:
        print('REQUEST TIMED OUT')