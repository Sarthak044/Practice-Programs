n_1=int(input('Enter a no.'))
rev=0
temp=n_1
while(temp>0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10

if(n_1==rev):
    print('Entered No. is pallindrome')
else:
    print('The entered no. is not pallindrome')