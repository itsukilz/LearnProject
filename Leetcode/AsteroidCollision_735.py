class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for x in asteroids:
            if len(stack) == 0:
                    stack.append(x)
            else:
                flag = 0
                while len(stack) != 0:
                    peek = stack[-1]
                    if (x>0 and peek>0) or (x<0 and peek<0) or (x>0 and peek<0):
                        stack.append(x)
                        flag = 0
                        break
                    elif abs(x) > abs(stack[-1]):
                        stack.pop()
                        flag = 1
                    elif abs(x) == abs(stack[-1]):
                        stack.pop()
                        flag = 0
                        break
                    else:
                        flag = 0
                        break
                if(len(stack)==0 and flag==1):
                    stack.append(x)
        return stack  

