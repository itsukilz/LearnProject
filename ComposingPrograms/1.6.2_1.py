def imporve(guess,tolerance):
	while(abs(guess*guess - (guess+1)) > tolerance):
		guess = 1.0/guess + 1
		print guess
	return guess

if __name__ == '__main__':
	print imporve(1,0.001)