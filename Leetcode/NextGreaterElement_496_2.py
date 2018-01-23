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

def nextGreaterElement(findNums, nums):
	# convert findNums to dic
	dic = {}
	for i in findNums:
		dic[i] = -1
	# convert nums to stack
	s = Stack()
	for i in nums[::-1]:
		s.push(i)

	temp = []
	while s.is_empty()==False:
		pop = s.peek()
		s.pop()
		
		if dic.get(pop,0)!=0:
			if s.size()==0:
				break
			else:
				peek = s.peek()
				# check all temp
				if len(temp)!=0:
					deltemp = []
					for i in temp:
						if peek > i:
							dic[i] = peek
							deltemp.append(i)
					for i in deltemp:
						temp.remove(i)

				if peek > pop:
					dic[pop] = peek

				else:
					temp.append(pop)

	result = []
	for i in findNums: 
		result.append(dic[i])
	return result

if __name__ == '__main__':
	print nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])