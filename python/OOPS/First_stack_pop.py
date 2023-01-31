stack = []

def push_val(val):
    stack.append(val)

def pop_val():
    val = stack[-1]
    del stack[-1]
    return val

push_val(1)
push_val(2)
push_val(3)

print(stack)

pop_val()

print(stack)