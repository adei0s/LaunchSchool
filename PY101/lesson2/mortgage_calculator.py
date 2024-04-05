# the formula is: 
#     m = p * (j / (1 - (1 + j) ** (-n)))

# reworded formula:
#     monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration)))

# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# get input from user for:
# loan_amount
# APR
# loan_duration

# divide APR by 12 to get monthly_rate

while True:
    
    loan_amount = float(input("What is the loan amount?\n"))
    
    APR = float(input("What is the percentage of the APR?\n"))
    
    loan_duration = float(input("What is the length of loan in months?\n"))
    
    monthly_rate = APR/100/12
    
    monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration)))
    
    result = f'your monthly payment is ${round(monthly_payment,2)}'
    
    print(result)
    
    again = input("another calculation? y/n \n").lower()
    
    if again == "y":
        continue
    
    elif again == "n":
        break
    
    else:
        again = input("please enter 'y' or 'n'.")