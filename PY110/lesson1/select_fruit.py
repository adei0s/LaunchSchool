def select_fruit(produce):
    fruit_lst = {}
    for fruit_key, fruit_value in produce.items():
        if fruit_value == 'Fruit':
            fruit_lst[fruit_key] = 'Fruit'
    return fruit_lst
        