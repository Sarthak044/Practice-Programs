class Stack:
    def __init__(self):
        self.__stack_list=[]
    
    def push_val(self,val):
        self.__stack_list.append(val)

    def pop_val(self):
        val =self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

#We want a new stack with new capabilities
#The first step is easy: just define a new subclass pointing to the class which will be used as the superclass.
#It gets all the components defined by its superclass

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push_val(self, val):
        self.__sum += val
        Stack.push_val(self, val)

    def pop_val(self):
        val = Stack.pop_val(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum

stack_object = AddingStack()

for i in range(5):
    stack_object.push_val(i)

print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop_val())
