def sqrt(a):
	def sqrt_update(x):
		return average(x, a/x)
	def sqrt_close(x):
		return approx_eq(x*x, a)
	return improve(sqrt_close, sqrt_update)

def average(x, y):
	return (x + y)/2.0

def approx_eq(x, y, tolerance=0.001):
	return abs(x - y)<tolerance

def improve(close, update, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess


print sqrt(256)