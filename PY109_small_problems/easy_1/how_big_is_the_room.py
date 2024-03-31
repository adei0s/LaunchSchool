# get input for length of room in meter
# get input for with of room in meter
# calculate room's area, then print it
# convert it to feet then print it

def invalid_num(number): #making sure input is a valid number
    try:
        number = float(number)
        if number <= 0:
            print('value must be a positive number')
            return True
    except ValueError:
        print('not a valid number')
        return True 
    return False
    
length = input("whats the length of the room: \n")

while invalid_num(length):
    length = input("whats the length of the room: \n")
length = float(length)
    
width = input("whats the width of the room: \n")
while invalid_num(width):
    width = input("whats the width of the room: \n")
width = float(width)
    
    
unit = input("what's the unit of measurement? enter 'm' for meter and 'f' for feet \n")

if unit == "f":
    length == length * 0.3048
    width == width * 0.3048
elif unit == "m":
    pass
else:
    unit = input("not a valid input, try again. enter 'm' for meter and 'f' for feet \n")
    

room_area = length * width
print(f"room's area is {room_area:.2f} square meters.")

area_in_feet = room_area * 10.7639
print(f"room's area in {area_in_feet:.2f} square feet.")