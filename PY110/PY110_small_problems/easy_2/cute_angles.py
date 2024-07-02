'''
given a floating num between 0 and 360
return str repr degree, min and seconds

whole digits are degree °
nums after floating point convert to minutes
subtract minutes from floating point num
convert to seconds


'''

DEGREE = "\u00B0"

def zeros(n):
    if int(n) == 0:
        return "00"
    elif int(n) < 10:
        return f'0{str(n)}'
    else:
        return str(n)

def dms(n):
    degree = int(n)
    minutes = int((n - degree) * 60)
    seconds = int(((n-degree)*60 - minutes) * 60)
    return(
        f'{degree}{DEGREE}'
        f"{zeros(minutes)}'"
        f'{zeros(seconds)}"')

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")