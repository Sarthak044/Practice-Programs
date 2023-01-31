'''a={'Name':'Sarthak','Age':19,'sign':'Saggi'}
print(a)
print('Enter the data')
a['Name']=input('Name= ')
print('Updated data')
print(a)'''

list_1=[]
for i in range(0,100):
    a=input(i)
    list_1.append(a)
odd= list(filter(lambda x: (x%2!=0),list_1))
print('odd no. in list is:\n',odd)