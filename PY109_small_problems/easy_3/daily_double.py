def crunch(string):
    while string:
        crunched = string[0]
        for letter in string:
            if letter != crunched[-1]:
                crunched += letter
        return crunched
    return ''

print(crunch(''))

