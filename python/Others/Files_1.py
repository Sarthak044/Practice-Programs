# File management in python 
#There are 4 modes 
#Read mode command used "r" :- Read only mode cannot modify the file 
#Write mode command used "w" :- This will write data to a file. Note that if the file already exists it will be erased! and overwritten
#append mode command used "a" :- This will put data at the end of a file
#Special read+ write command used "r+":- This mode has the ability to read and write to files

file = open(r"C:\Users\ASUS\Desktop\test.txt","r")
print(file.read())

#file.readlines() this will print out each line of the file that we have opened, or we can do file.readline() which will print 
#a line every time it is called, this can be called multiple times, to print the subsequent lines.
print("__________________________________")
file = open(r"C:\Users\ASUS\Desktop\test.txt","r")
print(file.readline())
print(file.readline())

print("___________________________________________")
print(file.readlines())

print("___________________________________________")

#using for loop
file=open(r"C:\Users\ASUS\Desktop\test.txt", "r")
for element in file:
    print(element, end='')
