# get student name and grades in (name, grade)
def process_student(student_data): 
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)
    
# get the average grade for a student
def average_grade(grades): #get the average grade for a student
    total = sum(grades)
    average = total / len(grades)
    return average

# a list of student, each student contain dict of their name:, and grade:
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

# 
def collect_grades(students):                   # given the list name students
    grades = []                                 # initiate an empty list named grades
    for student in students:                    # each item in the list of student
        name, grade = process_student(student)  # get name, grade
        if grade:
            grades.append(grade)                    # add that student's grade to the list 'grades'
    return grades                               # return the list of just grades

# call function collect_grades with arguement of the list 'students'. assign to var grades
grades = collect_grades(students)   

print(average_grade(grades))  # call function average_grade with argument of the list of 'grades' print result.


# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'