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
    data, address = sock.recvfrom(1024)
    print(data)
    temperature = data.decode("utf-8").split(":")
    try:
        temp = int(temperature[1])
        if temp > 35:
            message = (
                "message:" + temperature[0][13:] + " too hot!"
            )  # len(message from:) == 13
            sock.sendto(bytes(message, "utf-8"), (BROKER_IP, BROKER_PORT))
        if temp < 1:
            message = (
                "message:" + temperature[0][13:] + " too cold!"
            )  # len(message from:) == 13
            sock.sendto(bytes(message, "utf-8"), (BROKER_IP, BROKER_PORT))
    except Exception as e:
        pass
