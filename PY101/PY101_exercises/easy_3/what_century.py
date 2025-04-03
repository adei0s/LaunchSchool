def century(year):
    century_yr = (year//100) if (year % 100 == 0) else (year//100 + 1)

    if century_yr % 100 in (11, 12, 13):
        ends_with = "th"
    elif century_yr % 10 == 1:
        ends_with = "st"
    elif century_yr % 10 == 2:
        ends_with = "nd"
    elif century_yr % 10 == 3:
        ends_with = "rd"
    else:
        ends_with = "th"
        
    return (f'{century_yr}{ends_with}')

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")
