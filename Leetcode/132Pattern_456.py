def func(nums):
    length = len(nums)
    smaller,bigger = ["No"],["No"]*length
    stack = []
    for i in range(1,length):
        left = nums[i-1]
        if i==1:
            smaller.append(left)
        else:
            smaller.append(min(left,smaller[-1]))
    for i in range(length-1,1,-1):
        now = nums[i]
        left = nums[i-1]

        while stack and left>nums[stack[-1]]:
        	bigger[stack[-1]] = i-1
        	stack.pop()
        if left > now:
            bigger[i] = i-1
        else:
            stack.append(i)
    
    for i in range(2,length):
    	if bigger[i] != "No" and smaller[bigger[i]] != "No" and smaller[bigger[i]] < nums[i] :
    		return True
    return False

if __name__ == '__main__':
	print func([-1,3,2,0])