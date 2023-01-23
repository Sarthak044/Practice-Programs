list_1=[]
n=int(input('Enter the number of elements you want to have\n'))
for i in range(1,n+1):
    val=int(input('Enter the Elements'))
    list_1.append(val)

max=max(list_1[0],list_1[1]) 
secondmax=min(list_1[0],list_1[1]) 
  
for i in range(2,len(list_1)): 
    if list_1[i]>max: 
        secondmax=max
        max=list_1[i] 
    else: 
        if list_1[i]>secondmax: 
            secondmax=list_1[i] 
  
print("Second highest number is : ",str(secondmax)) 

    