for number in range(1, 99, 2):
    print(number)
    
# bonus:

starting_num = int(input('starting number: \n'))
ending_num = int(input('ending number: \n'))

for number in range(starting_num, ending_num):
    if number % 2 == 1:
        print(number)