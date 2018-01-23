def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for char in s:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if char == ")" and stack[-1]=="(":
                stack.pop()
            elif char == "}" and stack[-1]=="{":
                stack.pop()
            elif char == "]" and stack[-1]=="[":
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

if __name__ == '__main__':
    print isValid("()[]{()}")
    print isValid("[{}")