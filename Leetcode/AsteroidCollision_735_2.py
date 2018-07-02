def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for x in asteroids:
        stack = check(stack,x)

    return stack

def check(stack,x):
    if len(stack) == 0:
            stack.append(x)
            return stack
    else:
        peek = stack[-1]
        print peek,x
        if (x>0 and peek>0) or (x<0 and peek<0) or (x>0 and peek<0):
            stack.append(x)
            return stack
        elif abs(x) > abs(stack[-1]):
            stack.pop()
            return check(stack,x)
        elif abs(x) == abs(stack[-1]):
            stack.pop()
            return stack

if __name__ == '__main__':
    print  asteroidCollision([-2, -1, 1, 2])