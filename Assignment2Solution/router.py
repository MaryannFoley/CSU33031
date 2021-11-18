# Maryann Foley
# 19330904

import socket
import routes
import os
import select
from tlv import parseTLV

ip1 = os.environ['IP1']#input("Current IP Address:\t")
ip2 = os.environ['IP2']#input("Current IP Address:\t")
controller1 = os.environ['CIP1']
controller2 = os.environ['CIP2']

if not (ip1 and ip2):
    print("Set environment ip address.")
    quit()

BROKER_PORT = 51510

sock1 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock1.bind((ip1, BROKER_PORT))

sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock2.bind((ip2, BROKER_PORT))

socks=[sock1,sock2]

controllers = {sock1:controller1,sock2:controller2}

while True:
    ready_socks,_,_ = select.select(socks, [], [])
    for sock in ready_socks:
        data, addr = sock.recvfrom(1024) # This is will not block
        #print(dir(data))
        print ("received message:", data)
        #print(data)
        print("\nSender: "+addr[0] +" ("+routes.getCurrentName(addr[0]).decode("utf-8")+")")
        #print("Message: %s" % data)

        dest = parseTLV(data)
        nextIP=None
        print(dest)
        sock.sendto( bytes("10"+str(len(dest))+dest, "utf-8"), (controllers[sock], 51510))
        while not nextIP:
            contdata, contaddr = sock.recvfrom(1024)
            nextIP = parseTLV(contdata)
        print("nextip: "+nextIP)
        if len(nextIP) > 0:
            if nextIP.split(".")[1] == ip1.split(".")[1]:
                sock1.sendto(data, (nextIP, 51510))
            else:
                sock2.sendto(data, (nextIP, 51510))
        else:
            print("Lost :(")



# TLV : 1: Destination network
#        2: Message
#        3: From
