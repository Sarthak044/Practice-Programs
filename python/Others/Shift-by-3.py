#Step 1 input the string
text=input('Enter the string')

#step 2 Enter the shift
s=int (input('Enter the shift'))

#cipher Function

def encryption(string,s):
    cipher=''
    for i in string:
        if i==' ':
            print("Empty String passed, TRY AGAIN")
        elif i.isupper():
            cipher=cipher+chr((ord(i)+s-65)%26+65)
    return cipher

#Encrypted Code
print("Cipher Text is: \n",encryption(text,s))