'''
input: item id, and list of transactions
output: True if sum of qulitity value of item tranaction is > 0

'''
def transactions_for(item_id, transactions):
    return [item for item in transactions if item["id"] == item_id]
    
def is_item_available(item_id, transactions):
    item_transactions = transactions_for(item_id, transactions)
    available = 0
    for item in item_transactions:
        if item["movement"] == 'in':
            available += item["quantity"]
        elif item["movement"] == 'out':
            available -= item["quantity"]
    return available > 0
            
            
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True) 