'''
input: 3 numbers, thats the length of the 3 sides of a triangle


output: strings that classify the type of triangle as either 'equilateral',isosceles', sclene' or 'invalid'

- Equilateral: All three sides have the same length.
- Isosceles: Two sides have the same length, while the third is different.
- Scalene: All three sides have different lengths.

while none of the num are 0:

    if all 3 num are the same:
        return 'euquilateral'
    
    max(num) = largest side
    if max(num) < total num - max num:
        if num1 = num2 or num1 = num3 or num2 = num3:
            return 'isosceles'
        return 'scalene'
    return invalid
    
return invalid

'''

def triangle(num1, num2, num3):
    sides = [num1, num2, num3]
    if 0 in sides:
        return 'invalid'
    if len(set(sides)) == 1:
        return 'equilateral'
    elif max(sides) < sum(sides) - max(sides):
        if num1 == num2 or num1 == num3 or num2 == num3:
            return 'isosceles'
        return 'scalene'
    return 'invalid'
    
print(triangle(3, 3, 3))
print(triangle(3, 3, 1.5))
print(triangle(3, 4, 5))
print(triangle(0, 3, 3))
print(triangle(3, 1, 1))