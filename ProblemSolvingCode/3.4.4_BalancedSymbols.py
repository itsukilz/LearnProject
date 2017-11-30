#coding=utf-8
# page 70
class Stack:
    def __init__(self):
        self.items = [] #？ items

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


def BalancedSymbolChecker(string):
    checker = Stack()

    for i in string:
        if i in ['(','[','{','<']:
            checker.push(i)
        elif i != ' ':
            temp = checker.peek()+i
            if temp in ['()','[]','{}','<>']:
                checker.pop()
            else:
                return 0
    return 1


k = '{ { ( [ ] [ ] ) } ( ) }'
s = '[ { ( ) ]'  
print BalancedSymbolChecker(s)