num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
num3 = input("Enter the 3rd number: ")
num4 = input("enter the 4th number: ")
num5 = input("enter the 5th number: ")
num6 = input("enter the 6th number: ")

lst = [num1, num2, num3, num4, num5]

if num6 in lst:
    print(f"{num6} is in {','.join(lst)}")
else:
    print(f"{num6} isn't in {','.join(lst)}")
    

