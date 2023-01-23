rev = 0
x = int(input())
x1 = x
while(x>0):
    ld = x%10
    rev = (rev*10) + ld
    x = x//10
    
if rev == x1:
    print("true")
else:
    print("false")