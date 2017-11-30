#!/usr/bin/env python
# encoding: utf-8

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dic = {}
for i,t in enumerate(alpha):
    alpha_dic[t] = i+1

f = open("p022_names.txt")
line = f.readline().replace('"','').split(',')
line.sort()

count = 0
score = 0

for i in line:
    count += 1
    value = 0

    for c in i:
        value += alpha_dic[c]
    score += value * count

print score


