

def removeKdigits(num, k):
	if k == len(num):
		return "0"
	else:
		removeOrder = []
		outstring = ""
		count = 0
		while(count < k):
			for i in range(len(num)-1):
				if num[i] > num[i+1]:
					num = removeK(num,i)
					count += 1
					continue
		return num
def removeK(num,i):
	return num[:i] + num[i+1:]

if __name__ == '__main__':
	print removeKdigits("2354462",5)