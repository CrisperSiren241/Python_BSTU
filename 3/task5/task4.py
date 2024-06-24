# Напишите программу: 
# чтобы проверить, существует ли данный ключ в словаре;
#  для создания и отображения всех комбинаций букв, выбирая каждую букву из другого ключа в словаре, например, задан словарь {'1': ['a', 'b'], '2': ['c', 'd']}, результат: ac, ad, bc, bd; 
#  для замены значений словаря их средним значением.

my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'

if key_to_check in my_dict:
    print(f"Ключ '{key_to_check}' существует в словаре.")
else:
    print(f"Ключ '{key_to_check}' не существует в словаре.")

import itertools

my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = list(itertools.product(*[my_dict[key] for key in my_dict]))

print("Все комбинации букв из словаря:", combinations)

my_dict = {'a': 10, 'b': 20, 'c': 30}

mean_value = sum(my_dict.values()) / len(my_dict)

replaced_dict = {key: mean_value for key in my_dict}

print("Словарь с замененными значениями:", replaced_dict)

