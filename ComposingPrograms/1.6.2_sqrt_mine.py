def sqrt(a):
	return improve(square_close, sqrt_update, a)

def improve(close, update, a, guess=1):
	while not close(guess,a):
		print guess, a
		guess = update(guess,a)
	return guess

def square_close(guess,a):	
	return approx_eq(guess*guess, a)

def approx_eq(x, y, tolerance=0.001):
	return abs(x - y)<tolerance

def sqrt_update(x, y):
	return average(x, y/x)

def average(x, y):
	return (x + y)/2.0

if __name__ == '__main__':
	print sqrt(25)