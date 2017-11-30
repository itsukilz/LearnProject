#coding=utf-8
total = 200
start = [2,4,10,20,40,100,200]

route = []
result = []
count = 0

for a in range(start[0]+1):
	if 100*a > total:
		continue
	else:
		for b in range(start[1]+1):
			if 100*a + 50*b> total:
				continue
			else:		
				for c in range(start[2]+1):
					if 100*a + 50*b + 20*c > total:
						continue
					else:
						for d in range(start[3]+1):
							if 100*a + 50*b + 20*c + 10*d> total:
								continue
							else:
								for e in range(start[4]+1):
									if 100*a + 50*b + 20*c + 10*d + 5*e> total:
										continue
									else:
										for f in range(start[5]+1):
											if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f> total:
												continue
											else:
												temp = total - (100*a + 50*b + 20*c + 10*d + 5*e + 2*f)
												result.append([a,b,c,d,e,f,temp])
												count += 1

print count+1