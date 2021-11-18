# Maryann Foley
# 19330904

import socket
import routes
import os

ip = os.environ['IP']
if not ip:
	print("Set environment ip address.")
	quit()

#input("Current IP Address:\t")
#name = input("Current User Name:\t")

UDP_PORT = 51510

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((ip, UDP_PORT))


while True:
    data, address = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data,flush=True)

    #loopback
