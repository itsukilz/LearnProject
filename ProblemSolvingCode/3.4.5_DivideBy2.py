import Stack

def convert2binary(num):
    rem = Stack.Stack()
    result = ''
    while num > 0:
        remainer = num % 2
        num = num // 2
        
        rem.push(remainer)
    
    while rem.is_empty() != 1:
        result += str(rem.peek())
        rem.pop()
                
    return result


print convert2binary(233)