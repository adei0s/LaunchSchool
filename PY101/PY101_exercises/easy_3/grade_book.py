def get_grade(num1, num2, num3):
    average = (num1+num2+num3)/3
    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 70 <= average < 80:
        grade = "C"
    elif 60 <= average < 70:
        grade = "D"
    else:
        grade = "F"
    return grade


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")

            