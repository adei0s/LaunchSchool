def multisum(number):
    total_sum = 0
    for num in range(1, number+1):
        if (num % 3 or num % 5) == 0:
            total_sum += num
    return total_sum
