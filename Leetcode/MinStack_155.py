class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainstack = []
        self.minimum = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.minimum) == 0:
            self.minimum.append(x)
        else:
            self.minimum.append(min(self.minimum[-1],x))
        self.mainstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.mainstack.pop()
        self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mainstack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]

if __name__ == '__main__':
	obj = MinStack()
	obj.push(-2)
	obj.push(0)
	obj.push(-3)
	print obj.getMin()
	obj.pop()
	print obj.getMin()
