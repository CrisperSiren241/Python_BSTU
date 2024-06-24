# Напишите программу: 
# для объединения словарей в один новый словарь; 
# для сортировки словаря по значению;
# чтобы очистить список значений в словаре, если значениями словаря являются списки.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}

print("Объединенный словарь:", merged_dict)

my_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Отсортированный словарь по значению:", sorted_dict)

my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': 6}

cleaned_dict = {key: value if not isinstance(value, list) else [] for key, value in my_dict.items()}

print("Словарь после очистки списков в значениях:", cleaned_dict)
