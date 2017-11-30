#!/usr/bin/env python
# encoding: utf-8

date = ["m","t","w","th","f","sa","su"]
month_unleap =[3,0,3,2,3,2,3,3,2,3,2,3]
month_leap =[3,1,3,2,3,2,3,3,2,3,2,3]

allcount = 0
count1900 = 0
month = []
first_of_month = 0

for year in range(1900,2001):
    if year > 1900:
        first_of_month += month[-1]
        first_of_month %= 7
        if first_of_month == 6:
            allcount += 1

    print year,first_of_month
    #check leap year
    if year % 4 == 0:
        if year % 100 == 0 :
            if year % 400 == 0:
                month = month_leap
            else:
                month = month_unleap
        else:
            month = month_leap
    else:
        month = month_unleap

    for i in month[:-1]:
        first_of_month += i
        first_of_month %= 7
        print year,i,first_of_month
        if first_of_month == 6:
            allcount += 1
            if year == 1900:
                count1900 += 1

print allcount-count1900
