#coding=utf-8

def check_equal(a,b):
	la = list(a)
	lb = list(b)
	la.sort()
	lb.sort()
	return la == lb

def main():
	x = 1
	while True:
		x1 = str(x)
		x2 = str(2*x)
		if check_equal(x1,x2) == True:
			x3 = str(3*x)
			if check_equal(x1,x3) == True:
				x4 = str(4*x)
				if check_equal(x1,x4) == True:
					x5 = str(5*x)
					if check_equal(x1,x5) == True:
						x6 = str(6*x)
						if check_equal(x1,x6) == True:
							return x
		x += 1
print main()