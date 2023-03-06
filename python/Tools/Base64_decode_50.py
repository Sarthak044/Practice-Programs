# this file is encoded 50 times in base 64 

import base64

file = open(r"E:\Downloads\b64.txt", "r")

flag = file.read()

code = ""

for i in range(0,50):
    code = base64.b64decode(flag)
    flag = code

print(flag)