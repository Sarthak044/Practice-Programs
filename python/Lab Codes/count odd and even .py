list_1=[]
e_count=0
o_count=0
n=int(input('Enter the number of elements you want to have\n'))
for i in range(1,n+1):
    val=int(input('Enter the Elements'))
    list_1.append(val)
    
for j in list_1:
    if j%2==0:
        e_count+=1
    else:
        o_count+=1

print('Odd elements : ', o_count)
print('even elements : ', e_count)

    