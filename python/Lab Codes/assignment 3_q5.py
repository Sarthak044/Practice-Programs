#to combine 2 lists to create a dictionary 

#first list as key 
list_1=[]
x=int(input('Enter the number of key elements you want to have'))
for i in range(0,x):
    y=input('enter the keys')
    list_1.append(y)

#second list
list_2=[]
print('Enter the values to keys respectively')
for i in range(0,x):
    b=input()
    list_2.append(b)

#dictionary
dic_1={}
for i in list_1: 
    for j in list_2: 
        dic_1[i] = j 
        list_2.remove(j) 
        break  
#printing out the dictionary
print(dic_1)