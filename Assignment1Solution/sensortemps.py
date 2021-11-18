# Maryann Foley
# 19330904

import socket

IP = "172.20.0.4"
PORT = 49000

temperature = input("Current temperature:\t")

message = b"message:" + bytes(temperature, "utf-8")

print("Destination: " + IP + ":" + str(PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(message, (IP, PORT))
