n_1=int(input('Enter a no.'))
rev=0
temp=n_1
while(temp>0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
print('reverse of a given no is=',rev)