#!/usr/bin/python3

import socket
import sys
from datetime import datetime

# Define our target 
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to Ipv4

else:
    print("[+]Syntax port_Scanner.py <IP/HOSTNAME>\n")
    print("[+]Invalid Arguments. Exiting...")
    sys.exit()

# Banner
print("-" * 50)
print("Scanning {}...".format(target))
print("TimeStamp @ {}".format(str(datetime.now())))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print("Checking on port {}".format(port))
        if result == 1:
            print("[+]Port {} is open.".format((port)))
        s.close()

except KeyboardInterrupt:
    print("[+] ctrl+c detected... Exiting")
    sys.exit()

except socket.gaierror:
    print("[+] Hostname cannot be resolved")
    sys.exit()

except socket.error:
    print("[+] Couldn't connect to server.")
    sys.exit()