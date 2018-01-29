from itertools import combinations

def removeKdigits(num, k):
	k = combinations(num, len(num)-k)
	small = None
	for i in k:
		current = ""
		for j in i:
			current += j
		num_current = int(current)
		if small is None :
			small = num_current
		else:
			if int(current) < small:
				small = num_current
	return small

if __name__ == '__main__':
	print removeKdigits("2354462",5)