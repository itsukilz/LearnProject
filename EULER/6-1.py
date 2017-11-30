#coding=utf-8
import sys


def sumOfSquare(NUM):
	return (NUM*(NUM+1)*(2*NUM+1))/6 

def squareOfSum(NUM):
	return ((NUM*(NUM+1))/2)*((NUM*(NUM+1))/2)

if __name__ == '__main__':
	NUM = int(sys.argv[1])
	sumOfSquare = sumOfSquare(NUM)
	squareOfSum = squareOfSum(NUM)

	print abs(sumOfSquare - squareOfSum)