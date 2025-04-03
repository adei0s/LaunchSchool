'''
input: a number that is a year after 1752
output: number of friday 13th

plug in the year, iterate through the 13th off each month and tally how many of those are friday
'''

import datetime

def friday_the_13ths(year):
    count = 0
    for month in range(1, 13):
        x = datetime.datetime(year, month, 13)
        if x.strftime("%a") == "Fri":
            count += 1
    return count


        
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # Tru