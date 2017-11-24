def f(n,d):
	sn = list(str(n))
	sd = list(str(d))
	cp_sn = list(str(n))
	#if all the same
	if set(sn) == set(sd):
		return False
	else:
		if sn[0] in sd:
			sd.remove(sn[0])
			cp_sn.remove(sn[0])
		if sn[1] in sd:
			sd.remove(sn[1])
			cp_sn.remove(sn[1])

		if len(sd) == 2 :
			return False
		elif sd[0] == '0':
			return False
		else:
			return (cp_sn[0],sd[0])

def main():
	result = []
	for d in range(11,100):
		for n in range(10,d):
			if d%10 == 0 and n % 10 == 0:
				continue
			else:
				x = (n,d)
				y = f(n,d)
				#print x,y
				if y != False:
					if float(x[0])/float(x[1]) == float(y[0])/float(y[1]) :
						result.append(y)

	print result
main()