#!/bin/python3

#Imports
import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    #This is gonna translate the hostname into an IPv4
    Target = socket.gethostbyname(sys.argv[1])
else:
    print ("Invalid amount of arguments")
    print ("Closing...")
    sys.exit()

#Adding our banner
print ("*" * 40)
print ("Welcome to Pablo's Port Scanner!!")
print ("Your target is: " + Target)
print ("Time started: " + str(datetime.now()))
print ("*" * 40)

#Asking about the ports range to analyze
print ("\nPlease introduce the starting port")
StartPort = input()

print ("Please introduce the final port")
FinalPort = input()

#For-loop to send and receive packets
try:
    for Port in range(int(StartPort),int(FinalPort)):
        Packet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.2) # == 0.2
        #$Result will throw an error indicator
        Result = Packet.connect_ex((Target,Port))

        if (Result == 0):
            print ("The port {} is open".format(Port))
        Packet.close()

#Possibles exceptions
#Close with ctrl + c
except KeyboardInterrupt:
    print ("\nExiting program...")
    sys.exit()

#We can't connect to the hostname
except socket.gaierror:
    print ("\nHostname could not be resolved")
    sys.exit()

#If server is down
except socket.error:
    print ("\nCouldn't connect to server")
    sys.exit()

#Additional info to display
print ("The rest of the ports scanned are closed")