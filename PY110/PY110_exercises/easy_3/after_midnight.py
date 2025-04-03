'''
input: integer representing munutes to or from midnight
output: time of day in 24 hour format

- convert to hours: minutes. modulo hour by 24
- if positive, send
- if negative, subtract from 24:00
'''

def pad_zero(num):
    if num < 10:
        return f'{num:02d}'
    else:
        return f'{num}'

def time_of_day(num):
    num = num % 1440
    if num < 0:
        num = 1440 - num

    hours = num // 60
    minutes = num - (hours * 60)
    hours = hours % 24
    
    return f'{pad_zero(hours)}:{pad_zero(minutes)}'
    
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")  