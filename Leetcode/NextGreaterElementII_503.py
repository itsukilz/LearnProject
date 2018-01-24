def nextGreaterElements(nums):

	lnum = len(nums)
	temp, result = [], [-1]*lnum
	for i in range(2*lnum-1):
		now = nums[i%lnum]
		nex = nums[(i+1)%lnum]
		while temp and nex > nums[temp[-1]] and i+1 < temp[-1]+lnum:
			result[temp.pop()] = nex
		if i < lnum:
			if nex > now:
				result[i] = nex
			else:
				temp.append(i)
	return result
if __name__ == '__main__':
	print nextGreaterElements([4,5,7,8,1,7,6])