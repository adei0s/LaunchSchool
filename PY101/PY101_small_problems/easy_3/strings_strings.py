def stringy(num):
    count = 0
    string = ""
    while count < num:
        string += "1"
        count += 1
        if count < num:
            string += "0"
            count +=1
    return(string)


# alternate solution

def stringy(num):
    result = ""
    for digit in range(num):
        result += "0" if digit % 2 == 1 else "1"
    return result
                
# def string(num):
#     result = ""
#     ressult += "1" for digit in range(num) if digit % 2 ==1 else result += 0

print(stringy(2))