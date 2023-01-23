'''
#type 1
a=[1,2,3,4]
print(type(a))
print(type(a[2]))

#type 2
b=['hi',23,3.3,'yo']
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))

str1='coder'
list1=list(str1)
str2='yo'
list2=list(str2)
list3=list1+list2
print(list3)
'''

c='computer science'
c=list(c)
print(c[:])
print(c[1:2])
print(c[::-1])
print(c[-1])
print(c[-1:-5:-1])
print(c[::2])
print(len(c))
d=[22,12,2,213,123]
print(sum(d))
print(max(d))
print(min(d))
print(sorted(d))
d.append(33)
print(d)
print(d.count(33))
d.insert(3,4)
print(d)
print(d.index(4))
