# Maryann Foley
# 19330904

import socket

UDP_IP = "172.20.0.5"
UDP_PORT = 49000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

subscribe = input("Subscribe to dashboard? (y/n)\t")


BROKER_IP = "172.20.0.4"
BROKER_PORT = 49000

if subscribe == "y":
    message = "subscribe:dashboard"
    sock.sendto(bytes(message, "utf-8"), (BROKER_IP, BROKER_PORT))

while True:
    data, address = sock.recvfrom(1024)
    print(data, flush=True)
