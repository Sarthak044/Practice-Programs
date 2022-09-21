#!/usr/bin/python3

import socket

host = '127.0.0.1'
port = 5000

# AF_INET means that we are connecting over IPv4 connection 

# We can think of SOCK_STREAM as a port 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection
s.connect((host,port))

