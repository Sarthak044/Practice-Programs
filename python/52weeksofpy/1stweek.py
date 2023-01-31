from pprint import pprint

device = {
    "name":"sarthak",
    "vendor":"cisco",
    "model":"nexus",
    "os":"mexus20.v"}

#print("device",device)
#print("device name", device["name"])

#pprint(device) #alphabetical order

for key, value in device.items():
    print("{:>15s}:{}".format(key,value))

