#To find out smallest
list_1=[]
n=int(input('Enter the number of elements you want to have\n'))
for i in range(1,n+1):
    val=int(input('Enter the Elements'))
    list_1.append(val)

print('Smallest no. in the list is : ',min(list_1))

#To find out the largest no.
print('largest no. in the list is : ',max(list_1))

    
