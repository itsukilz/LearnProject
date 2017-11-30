#coding=utf-8
# implement of stack
class Stack:
    def __init__(self):
        self.items = [] #？ 我其实还是没有搞懂，为什么这里是items

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
