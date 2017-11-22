#coding = utf-8
count = 2
a = 1
b = 1

while True:
	c = a + b
	count += 1

	if len(str(c)) >= 1000:
		print count
		break
	else:
		a = b
		b = c