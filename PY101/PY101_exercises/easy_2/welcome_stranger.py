def greetings(name, dictionary):
    return (f'Hello, {" ".join(name)}! Nice to have a {dictionary["title"]} {dictionary["occupation"]} around.')
    
    
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)