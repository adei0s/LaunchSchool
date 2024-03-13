import json

def prompt(message):
    print(f"==> {message}")

def invalid_num(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False
    
def calculation(operation_num):
    match operation_num:
        case '1':
            result = int(num1) + int(num2)
        case '2':
            result = int(num1) - int(num2)
        case '3':
            result = int(num1) * int(num2)
        case '4':
            result = int(num1) / int(num2)
    return result
    
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)
    
def messages(message, lang='en'):
    return MESSAGES[lang][message]
    
prompt(messages('welcome'))

while True:
    prompt(messages("num1_prompt"))
    num1 = input()
    
    while invalid_num(num1):
        prompt(messages("invalid_num"))
        num1 = input()
    
    prompt(messages("num2_prompt"))
    num2 = input()
    
    while invalid_num(num2):
        prompt(messages("invalid_num"))
        num2 = input()
    
    prompt(messages("operation_prompt"))
    operation = input()
    
    while operation not in ['1', '2', '3', '4']:
        prompt(messages("invalid_op_prompt"))
        operation = input()
        
    result = calculation(operation)
    
    prompt(messages("result").format(result=result))
    
    prompt(messages("again_prompt"))
    again = input()
    
    if again == "Y":
        continue
    elif again == "N":
        break
    else:
        prompt("enter 'Y' or 'N'")
        again = input()
    
    
    
    