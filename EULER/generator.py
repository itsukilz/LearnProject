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

