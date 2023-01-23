#!/usr/bin/python3

from sys import argv
import subprocess

if len(argv) == 1:
    print('''enter a valid arg s/f\n
            s --> compact form
            f --> original logs with request and result body''')
    exit()

def remove(data, start, end):
    while True:
        s_index = data.find(start)
        if s_index == -1:
            break
        e_index = data.find(end, s_index)
        data = data[:s_index] + data[e_index:]
    return data

try:
    containerId = input("Enter Container ID -- >\t")
    tail = input("tail value -- >\t")
    log1 = subprocess.run(['docker', 'logs',containerId, '--follow', '--timestamps', '--tail',tail], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    #exit()

    data = log1
    for i in argv:
        print(i)

    if argv[1] == 'f':
        print("hello f")
        print(data)
        exit()

    elif argv[1] == 's':
        print("hello s")
        data = remove(data, "result", "}")
        data = remove(data, "Request", "}")
        print(data)
        exit()

    else:
        print('''enter a valid arg s/f\n
                s --> compact form
                f --> original logs with request and result body''')
        exit()


except KeyboardInterrupt():
    print("Closing..")   
    exit()
    
    '''print("Save Logs?y/n")
        save = ''
        if save == 'y':
            subprocess.call(["touch", "Logsfile.txt"])
            file1 = open("LogsFile.txt", "w")
            file1.write(data2)
            file1.close()
            #data2 = remove(log1)
            #write = print(data2)
            #subprocess.call([write, ">>", "Savelog.txt"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    '''