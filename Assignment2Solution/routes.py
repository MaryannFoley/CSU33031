routes = {
    "172.18.0.3" :
    {
        "172.18.0.2" : "172.18.0.3",
        "172.19.0.2" : "172.18.0.3",

        "172.19.0.3" : "172.19.0.2",
        "172.21.0.2" : "172.19.0.2",

        "172.21.0.3" : "172.21.0.2",
        "172.22.0.2" : "172.21.0.2",

        "172.22.0.3" : "172.22.0.2",
    },

    "172.22.0.3" :
    {
		"172.18.0.3" : "172.18.0.2",

        "172.18.0.2" : "172.19.0.3",
        "172.19.0.2" : "172.19.0.3",

        "172.19.0.3" : "172.21.0.3",
        "172.21.0.2" : "172.21.0.3",

        "172.21.0.3" : "172.22.0.3",
        "172.22.0.2" : "172.22.0.3",

    }

}

names = {
	"E1" : "172.18.0.3",
	"E2" : "172.22.0.3",
	"R1" : "172.18.0.2",
	"R2" : "172.19.0.3"
}

userInitialRoutes = {
	"172.20.0.2" : "172.20.0.4",
	"172.20.0.3" : "172.20.0.5"
}

def next (current, destination):
	return routes[destination][current]

def getip(name):
	return names[name]

def getCurrentName (ip):
	for name in names.keys():
		if names[name] == ip:
			return bytes(name, "utf-8")
	return b"Not Found"

def getInitialRoute(ip) :
	if ip in userInitialRoutes:
		return userInitialRoutes[ip]
	return "cannot get route"

# routes = { destination : {in : out}}

#CONTROLLER
#172.18.0.4, 172.19.0.4, 172.21.0.4, 172.22.0.4

#ENDUSER1
#export IP=172.18.0.3
#export CIP=172.18.0.4

#ROUTER1
#export IP1=172.18.0.2
#export IP2=172.19.0.2
#export CIP1=172.18.0.4
#export CIP2=172.19.0.4

#ROUTER2
#export IP1=172.19.0.3
#export IP2=172.21.0.2
#export CIP1=172.19.0.4
#export CIP2=172.21.0.4

#ROUTER3
#export IP1=172.21.0.3
#export IP2=172.22.0.2
#export CIP1=172.21.0.4
#export CIP2=172.22.0.4

#ENDUSER2
#export IP=172.22.0.3
#export CIP=172.22.0.4

#CONTROLLER (num routers + 1 ips)
#export IPs=172.19.0.4,172.18.0.4,172.21.0.4,172.22.0.4
