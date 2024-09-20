'''
input: 3 num thats the 3 angles of a triangle

out: strings that classify the triangle as 'right', 'acute', 'obtuse' or 'invlid'

angles = [num1, num2, num3]

if 0 in angles or sum(angles) != 180:
    return invlid
elif max(angles) > 90:
    return obtuse
elif max(angles) == 90:
    return right
else:
    return acute
    
'''

def triangle(num1, num2, num3):
    angles = [num1, num2, num3]
    
    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    elif max(angles) > 90:
        return 'obtuse'
    elif max(angles) == 90:
        return 'right'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")