#!/bin/python3

#Imports
import urllib.request
import json
import sys
from datetime import datetime

#We are going to use one website called ipinfo.io to extract data in json format
#Then we are going to prepare that info for the user to read easily

def main():
    print ("Introduce your target in IPv4 format")
    IPv4 = input()

    #Adding our banner
    print ("\n" + "*" * 40)
    print ("Welcome to Pablo's IP Geolocator!!")
    print ("Your target is: " + IPv4)
    print ("Time started: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print ("*" * 40 + "\n")

    Target = "https://ipinfo.io/" + IPv4 + "/json"

    #We are extracting the json data from Target URL
    UrlLibObject = urllib.request.urlopen(Target)
    JsonInfo = json.loads(UrlLibObject.read())

    for Data in JsonInfo:
        #We dont want to show the "Readme info"
        if Data != "readme":
            print (Data.title() + " : " + JsonInfo[Data])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()