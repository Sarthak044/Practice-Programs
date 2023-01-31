

from re import X
import sys

log1 = open("E:\Sarthak\Coding\Python\kassio_scripts\logs_sample.txt", "r")
 
#read whole file to a string
data = log1.read()
# print(data)
# response = ""
if len(sys.argv) == 1:
    print("enter a valid arg s/f")
    exit()
if sys.argv[1] == 'f':
    print(data)
    log1.close()
    exit()
elif sys.argv[1] == 's':
    while True:
        s_index = data.find("result")
        if s_index == -1:
            break
        e_index = data.find("}", s_index)
        data = data[:s_index] + data[e_index:]
        # response+=log1[last:s_index]
        # last = e_index
    while True:
        s_index = data.find("Request")
        if s_index == -1:
            break
        e_index = data.find("}", s_index)
        data = data[:s_index] + data[e_index:]
else:
    print("enter a valid arg s/f")
    exit()


data = remove(data, "result", "}")
data = remove(data, "Request", "}")
 
remove(data, start, end):
    while True:
        s_index = data.find(start)
        if s_index == -1:
            break
        e_index = data.find(end, s_index)
        data = data[:s_index] + data[e_index:]
    return data


print(data)

log1.close()

#print("hello\nhhhhha ")

