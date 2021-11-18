import socket
import routes
import os
import select
import routingTable
from tlv import parseTLV

PORT = 51510

ips = os.environ['IPs']

controlips = ips.split(",")

socks = []
for ip in controlips:
    newSock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    socks.append(newSock)
    socks[-1].bind((ip, PORT))

while True:
    ready_socks,_,_ = select.select(socks, [], [])
    for sock in ready_socks:
        data, addr = sock.recvfrom(1024) # This is will not block
        print ("received message:", data)

        dest=parseTLV(data)

        nextStep = routes.next( addr[0],routes.getip(dest))
        print("nextStep: "+nextStep)

        if len(nextStep) > 0:
            sock.sendto(bytes("4"+str(len(nextStep))+nextStep, "utf-8"), (addr[0], 51510))
        else:
            print("Lost :(")
