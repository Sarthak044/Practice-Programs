#5 times encoded using base 64
#5 times encoded using base 32

#5 times encoded using base 16!

import base64

file = open(r"E:\Downloads\encodedflag.txt", "r")

flag = file.read()

code=""

for i in range(0,5):
    code = base64.b16decode(flag)
    flag = code

for i in range(0,5):
    code = base64.b32decode(flag)
    flag = code

for i in range(0,5):
    code = base64.b64decode(flag)
    flag = code

print(flag)
file.close()
