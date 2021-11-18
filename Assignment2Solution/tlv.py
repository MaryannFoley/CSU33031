def parseTLV(tlv):
    tlv = tlv.decode("utf-8")
    while len(tlv) > 0:
        typep = int(tlv[0])
        lenp = int(tlv[1:3])
        messagep = tlv[3:lenp+3]
        print("tlv: "+tlv+" message: "+messagep)

        if typep == 1: # If type == destination network
            return messagep
        if typep == 4:
            return messagep

        tlv = tlv[lenp+2]


# TLV : 1: Destination network
#		2: Message
#		3: From
#		4: Network Step
