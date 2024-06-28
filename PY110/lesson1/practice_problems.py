# problem 1
fruits = ("apple", "banana", "cherry", "date", "banana")

count = fruits.count("banana")

# problem 3
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

set_ab = a | b

print(set_ab)

# problem 5
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

sum(ages.values())

# problem 6

min(ages.values())

# problem 8

statement = "The Flintstones Rock"
def char_frequency(statement):
    statement_dict = {}
    statement - statement.replace(' ', '')
    for char in statement:
        statement_dict[char] = statement_dict.get(char, 0) + 1
    return statement_dict
    