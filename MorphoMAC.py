#!/usr/bin/env python3

import os
import sys
import time
import subprocess

try:
    import requests
except ImportError:
    subprocess.run(['pip', 'install', 'requests'])
    import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

def get_old_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    result = result.decode('utf-8')
    mac_index = result.find("ether") + 6
    return result[mac_index:mac_index+17]

logo = """
\033[1;35m
                                                                                                 
 _|      _|                                _|                  _|      _|    _|_|      _|_|_|  
 _|_|  _|_|    _|_|    _|  _|_|  _|_|_|    _|_|_|      _|_|    _|_|  _|_|  _|    _|  _|        
 _|  _|  _|  _|    _|  _|_|      _|    _|  _|    _|  _|    _|  _|  _|  _|  _|_|_|_|  _|        
 _|      _|  _|    _|  _|        _|    _|  _|    _|  _|    _|  _|      _|  _|    _|  _|        
 _|      _|    _|_|    _|        _|_|_|    _|    _|    _|_|    _|      _|  _|    _|    _|_|_|  
                                 _|                                                            
                                 _|                                                            
\033[1;31m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m DEVELOPED By \033[1;31m(\033[1;33mKaran_Parelkar\033[1;31m)~~~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m Join me :- \033[1;31m(\033[1;33mhttps://github.com/KaranParelkar \033[1;31m)~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print(logo)
hprint("Starting MorphoMAC Tool for changing MAC address of your device....")
time.sleep(1)
print("")
net = input("Choose your network connection type\n1. eth0\n2. wlan0\n3. exit\n")

if net == '1':
    old_mac = get_old_mac("eth0")
    new_mac = input("Enter the new MAC address > ")
    print("{+} Changing MAC address for eth0 from " + old_mac + " to " + new_mac)
    subprocess.run(["ifconfig", "eth0", "down"])
    subprocess.run(["ifconfig", "eth0", "hw", "ether", new_mac])
    subprocess.run(["ifconfig", "eth0", "up"])

elif net == '2':
    old_mac = get_old_mac("wlan0")
    new_mac = input("Enter the new MAC address > ")
    print("{+} Changing MAC address for wlan0 from " + old_mac + " to " + new_mac)
    subprocess.run(["ifconfig", "wlan0", "down"])
    subprocess.run(["ifconfig", "wlan0", "hw", "ether", new_mac])
    subprocess.run(["ifconfig", "wlan0", "up"])
    
elif net == '3':
    print("Exiting...")
    sys.exit()
    
else:
    print(" Please Enter a valid option!!!!")
