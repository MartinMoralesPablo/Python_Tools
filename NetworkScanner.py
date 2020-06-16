#!/bin/python3

#Imports
from scapy.all import *
import argparse
from datetime import datetime

#By arguments, we are going to collect a network and we are going to be able
#to see all the devices which are connected to it

Parse = argparse.ArgumentParser()
Parse.add_argument("-n", "--network", help="The network which is going to be analyzed")
Parse = Parse.parse_args()

def main():
    #Adding our banner
    print ("\n" + "*" * 40)
    print ("Welcome to Pablo's Network Scanner!!")
    print ("The selected network is: " + Parse.network)
    print ("Time started: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print ("*" * 40 + "\n")
    
    if Parse.network:
        Scan(Parse.network)
    else:
        print ("Arguments number invalid, please, check the help with the -h argument")
        exit()

def Scan(Network):
    IPRange = ARP(pdst=Network)
    Broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    FinalPacket = Broadcast/IPRange
    Result = srp(FinalPacket, timeout = 1, verbose=False)[0]

    print ("IP \t\t\t\t MAC \n" + "*" * 50)
    for IPScanned in Result:
        print ("[+] {} \t\t {}".format(IPScanned[1].psrc, IPScanned[1].hwsrc))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()