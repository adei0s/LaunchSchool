'''
input: list of integers between 0 and 19
output: list of int sorted based on he english word for each number

- list = arabic num : english num
- sort by english num

'''
NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def alphabetic_number_sort(input_list):
    return sorted(input_list, key = lambda x: NUMBERS[x]) 
    
print(alphabetic_number_sort(input_list))