#find numbers divisible 10 from a list using lamda function


list_1=[]
print('Enter the Number of elements you need ')
x=int(input())
for i in range(0,x):
    list_1.append(i)

cond=list(filter(lambda x: (x % 10 == 0), list_1))  
print('Numbers divisible from 10 are:')
print(cond)

