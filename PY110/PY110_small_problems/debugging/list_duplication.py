data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
unique_data = [item for item in data if item not in unique_data]
print(unique_data) # order not guaranteed