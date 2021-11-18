# Maryann Foley
# 19330904

import socket

BROKER_IP = "172.20.0.4"
BROKER_PORT = 49000

SENSORS = [
    (b"sensor1", "172.20.0.3"),
    (b"sensor2", "172.20.0.5"),
    (b"dashboard", "172.20.0.2"),
]
subscriptions = {"172.20.0.3": [], "172.20.0.5": [], "172.20.0.2": []}

# recieve
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((BROKER_IP, BROKER_PORT))

while True:
    data, address = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("\nSender: " + address[0])
    print("Message: %s" % data)
    if data.startswith(b"subscribe:"):
        print("New subscription")
        sensorName = data[10:]
        # print(sensorName)
        ip = [(name, address) for name, address in SENSORS if name == sensorName]
        if len(ip) > 0:
            subscriptions[ip[0][1]].append(address[0])
            # print(subscriptions)
        else:
            print("No such sensor")
        # print(subscriptions)
    elif data.startswith(b"message:"):
        print("New published message")
        ip = address[0]
        names = [(name, address) for name, address in SENSORS if address == ip]
        if len(names) > 0:
            sensorName = names[0][0]
        else:
            sensorName = bytes(ip, "utf-8")
        message = b"Message from " + sensorName + b":" + data[8:]
        if ip in subscriptions.keys():
            print("Being sent to " + str(len(subscriptions[ip])) + " subscriber(s)")
            for subscribed in subscriptions[ip]:
                sock.sendto(message, (subscribed, 49000))
        else:
            print("Sender does not have subscribers")
    else:
        print("Unrecognized command")

    # https://wiki.python.org/moin/UdpCommunication

# xhost + 127.0.0.1
