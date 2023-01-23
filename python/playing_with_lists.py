#Introduction
print('******* Welcome To My Program *********')

#Declaring a list 

list_1=[]
print('\t***Default the list is empty***\n')


#Options
print('Enter the choice\n')
opt_1=input('\t1.Add an Element.\n\t2.Delete an Element.\n\t3.To Sort the list.\n\t4.Replace a Element.\n\t5.Delete the whole list.\n\t6.To Exit\n')

def add_element():
    n=int(input('Enter the elements you want to have in your list'))
   
    for i in range(0, n):
        print("Enter element at location", i, ":")
        item = (input())
        list_1.append(item)
        print('Updated list\n',list_1)

#Funtion to Delete 
def delete_elements():
    item_1= input('Enter the element you want to delete\n')
    if  (item_1 in list_1):
        print('Deleting the Element...\n')
        list_1.remove(item_1)
        print('Element Deleted Successfully')
        print('Updated list\n',list_1)
    else:
        print('Element not present\n')
    
#function to Sort the list 
def sort(n=0):
    state=input('To Sort a list you must have only numbers or only strings in the list\n\tDO YOU HAVE BOTH?\n yes/no\n')
    if state=='yes':
        print('Cannot be sorted')
    
    elif state=='no':
        print('Select the sorting pattern\n')
        num=(input('Enter the number of the option you would like to choose\n\t1.Ascending.\n\t2.Descending\n'))
        if num=='1':
            list_1.sort()
            print(list_1)
        elif num=='2':
            print(list_1.sort(reverse=True))
        else:
            print('Not a Valid input')
            
    else:
        print('Invalid')

#Function to replace the number
def replace_1():
    rep_1=input('Enter the element you want to replace')           
    rep_2=input('Enter the element you want to remove')
    if rep_2 in list_1:
        print('Updating the element from the list...\n')
        list_1.remove(rep_2)
        list_1.insert(rep_1)
        print('Updated list\n',list_1)
    else:
        print('Element not present in the list')

#To delete the whole list 
def del_whole():
    state_1=input('ARE YOU SURE YOU WANT TO DELETE THE WHOLE LIST\n\tYes/No')
    if state_1=='Yes':
        print('Deleting the whole list..\n')
        list_1.clear()
        print('List is empty')
    else:
        print('Then why choose the option.. jeez!')

while True:
    if opt_1=='1':
        add_element()
        break
    elif opt_1=='2':
        delete_elements()
        break
    elif opt_1=='3':
        sort()
        break
    elif opt_1=='4':
        replace_1()
        break
    elif opt_1=='5':
        del_whole()
        break
    elif opt_1==6:
        print('Exited')    
        break


   

