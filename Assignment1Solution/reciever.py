# This file is only to recieve test messages, it will demonstrate one way transmission to the dashboard but not the response
# Maryann Foley
# 19330904

import socket

UDP_IP = "172.20.0.2"
UDP_PORT = 49000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

subscribe = input("Subscribe to:\t").split(",")


BROKER_IP = "172.20.0.4"
BROKER_PORT = 49000

for subscription in subscribe:
    message = "subscribe:" + subscription
    sock.sendto(bytes(message, "utf-8"), (BROKER_IP, BROKER_PORT))

while True:
    data, address = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print(data)
