#!/bin/python3
import sys #allow us to enter command line agreements 
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates host to ipv4
else:
	print("invalid amounts of elemnts")
	print("syntax: python3 scanner.py <ip>")
	sys.exit()
	
#Add a pretty banner
print("-"*50)
print("scanning port "+target)
print("time started :"+str(datetime.now()))
print("-"*50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result = s.connect_ex((target,port)) #returns errror indicator
		print("cheking the port {} ".format(port))
		if result == 0:
			print("port is open {} ".format(port))
			s.close
except KeyboardInterrupt:
	print("\n exiting program")
	sys.exit()
except socket.gaierror:
	print("host name cannot be resolved")
	sys.exit()
except socket.error:
	print("could not connect to server")
	sys.exit()
