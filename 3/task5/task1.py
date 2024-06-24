# Напишите программу:
#  для сортировки (по возрастанию и убыванию) словаря по значению; 
#  для объединения двух словарей и суммирующую значения для общих
# для проверки наличия нескольких ключей в словаре.

my_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("По возрастанию:", sorted_dict_asc)

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("По убыванию:", sorted_dict_desc)

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_dict = {**dict1, **dict2}
print("Объединенный словарь:", merged_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}

keys_to_check = ['a', 'd']

for key in keys_to_check:
    if key in my_dict:
        print(f"Ключ '{key}' присутствует в словаре.")
    else:
        print(f"Ключ '{key}' отсутствует в словаре.")

