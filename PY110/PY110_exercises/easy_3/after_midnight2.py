'''
two functions:
input: time of day in 24 hr format
output: before, and after mightnight in number of minutes
'''

def after_midnight(time):
    hours = int(time[:2])
    minutes = int(time[3:])
    total = (hours*60 + minutes)%1440
    return total
    
def before_midnight(time):
    return (1440 - after_midnight(time))%1440
    
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)