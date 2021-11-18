# This file is only to send a test message, it will demonstrate one way transmission to the dashboard but not the response
# Maryann Foley
# 19330904

import socket

IP = "172.20.0.4"
PORT = 49000
MESSAGE = b"message:A message from sensor 2."

print("Destination: " + IP + ":" + str(PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

sock.sendto(MESSAGE, (IP, PORT))
