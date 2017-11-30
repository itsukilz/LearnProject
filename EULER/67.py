#!/usr/bin/env python
# encoding: utf-8

#input number
f = open("p067_triangle.txt")
flines = f.readlines()
length = len(flines)
num =  []

for i in range(length):
    templine = flines[i].split(" ")
    templist = []
    for j in templine:
        templist.append(int(j))
    num.append(templist)

f.close()

# counting sum
for i in range(length-1,-1,-1):
    top = num[i-1]
    bottom = num[i]
    for j in range(i):
        top[j] += max(bottom[j],bottom[j+1])

print num[0][0]
