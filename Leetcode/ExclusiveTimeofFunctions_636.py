def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    dic = dict.fromkeys(range(n),0)
    stack = []
    for log in logs:
        loglist = log.split(":")
        logfunc = loglist[1]
        logx = (int(loglist[0]),int(loglist[2]))
        
        if logfunc == "start":
            stack.append(logx)

        else:
            peek = stack[-1]
            print log, stack
            dic[peek[0]] += logx[1]-peek[1]+1
            stack.pop()
            if len(stack)!=0:
                dic[stack[-1][0]] -= logx[1]-peek[1]+1

    result = []
    for i in range(n):
        result.append(dic[i])
    return result

if __name__ == '__main__':
    print exclusiveTime(1,["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])