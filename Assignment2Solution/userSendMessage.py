# Maryann Foley
# 19330904

import socket
import routes
import os
from tlv import parseTLV

PORT = 51510


ip = os.environ['IP']
cip = os.environ['CIP']
if not ip:
	print("Set environment ip address.")
	quit()


message = input("Message:\t")
destination = input("Destination:\t")

contcomp = b'102' + bytes(destination, "utf-8")
if len(message) >= 10:
	messagecomp = b'102' + bytes(destination, "utf-8")+ b'2'+bytes(str(len(message))+message, "utf-8")+b'202'+routes.getCurrentName(ip)
else:
	messagecomp = b'102' + bytes(destination, "utf-8")+ b'20'+bytes(str(len(message))+message, "utf-8")+b'202'+routes.getCurrentName(ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

nextIP=None
sock.bind((ip, PORT))
sock.sendto(contcomp, (cip, PORT))

while not nextIP:
	contdata, contaddr = sock.recvfrom(1024)
	print(contdata)
	nextIP = parseTLV(contdata)

if len(nextIP) > 0:
	print("Sending message to "+nextIP)
	sock.sendto(messagecomp, (nextIP, 51510))
