class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push_val(self, val):
        self.__stack_list.append(val)
    
    def pop_val(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object=Stack() 

stack_object.push_val(1)
stack_object.push_val(2)
stack_object.push_val(3)

print(stack_object.pop_val())
print(stack_object.pop_val())
print(stack_object.pop_val())

#to have multiple stack just creat more object
stack_object_1=Stack()
stack_object_2=Stack()