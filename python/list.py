a=[]
for i in range(0,6):
    x=input('Enter the numbers')
    a.append(x)

print('the list is as follows ')
print(a)
map(lambda s: s.split(':'), a)

