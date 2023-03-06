#upper case to lower case using lambda funtion

x=input('Enter a Word/Sentence\n')
func=lambda x:x.upper()
func_1=lambda x: x.lower()
if x.islower():
    print('Uppercase form of the following string is:')
    print(func(x))
else:
    print('Lower case of the following string is:')
    print(func_1(x))