import Stack

def DivideByBase(num,base):
    rem_stack = Stack.Stack()
    result_string = ''
    while num > 0:
        remainer = num % base
        num = num // base

        rem_stack.push(remainer)

    while rem_stack.is_empty() != 1:
        result_string += str(rem_stack.peek())
        rem_stack.pop()

    return result_string

#test
#233 351(8)
#print DivideByBase(233,8)

#233 14-9(16)
#print DivideByBase(233,16)


#3.4.6 selfcheck
print DivideByBase(25,8)

print DivideByBase(256,16)

print DivideByBase(26,26)
