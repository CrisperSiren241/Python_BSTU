# Напишите программу, которая принимает список словарей и объединяет их в один словарь.
list_of_dicts = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5}]

merged_dict = {}
for dictionary in list_of_dicts:
    merged_dict.update(dictionary)

print("Объединенный словарь:", merged_dict)
