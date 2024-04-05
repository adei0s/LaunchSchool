def twice(num):
    num_str = str(num)
    mid = len(num_str)//2
    if (num_str[:mid] == num_str[mid:]):
        result = num
    else: 
        result = num * 2
    return result

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)