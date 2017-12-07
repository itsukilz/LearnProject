def gen_pandigital(digits=9):
	"""generates pandigital numbers starting with the biggest"""
	
	def generator(start, digits_left):
		if len(digits_left) == 1:
			yield int(start + digits_left[0])
		else:
			for i in digits_left:
				for p in generator(start + i, filter(lambda x: x != i, digits_left)):
					yield p

	digits = [str(i) for i in range(digits,-1,-1)]
	for i in generator("",digits):
		yield i


def main():
	allsum = 0
	prime = [2,3,5,7,11,13,17]
	for number in gen_pandigital():
		flag  = 1
		for i in range(1,8):
			temp = str(number)[i:i+3]
			tempprime = prime[i-1]

			if int(temp) % tempprime != 0:
				flag = 0
				break

		if flag == 1:
			allsum += number
		else:
			continue

	print allsum

def test():
	allsum = 0
	prime = [2,3,5,7,11,13,17]
	number = 9546071328
	flag  = 1
	for i in range(1,9):
		temp = str(number)[i:i+3]
		tempprime = prime[i-1]
		print temp,tempprime
		if int(temp) % tempprime != 0:
			flag = 0
			break
	if flag == 1:
		allsum += number

	print allsum
main()