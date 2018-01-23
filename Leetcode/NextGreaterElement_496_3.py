#coding=utf-8
# implement of stack
def nextGreaterElement(findNums, nums):
	# convert findNums to dic
	dic = {}
	for i in findNums:
		dic[i] = -1

	temp = []
	length = len(nums)
	
	for i in range(length):
		pop = nums[i]
		if dic.get(pop,0)!=0:
			if i==length-1:
				break
			else:
				peek = nums[i+1]
				# check all temp
				while temp and temp[-1] < peek:
					dic[temp[-1]] = peek
					temp.pop()
				
				if peek > pop:
					dic[pop] = peek
				else:
					temp.append(pop)

	result = []
	for i in findNums: 
		result.append(dic[i])
	return result

if __name__ == '__main__':
	print nextGreaterElement([4,7,5],[5,4,7,2,1,6])