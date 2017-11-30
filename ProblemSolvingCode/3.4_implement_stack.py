class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def pop(self):
        del self.items[len(self.items)-1]

    def show(self):
        return self.items

# rev_string

def rev_string(my_string):

    s = Stack()
    my_str_list =  list(my_string)

    length = len(my_str_list)

    for i in range(length):
        temp = my_str_list[i]
        print temp
        s.push(temp)

    new_string = ''

    while not s.is_empty():
        new_string += s.peek()
        s.pop()
                    
    return new_string


print rev_string('help')