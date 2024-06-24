# Напишите программу:
# чтобы получить максимальное и минимальное значение в словаре; 
# для печати в отдельные строки ключей и значений словаря; 
# для создания словаря ключей x, y и z, где каждый ключ имеет значение списка из 11–20,21–30 и 31–40 соответственно.
# Получите доступ к пятому значению каждого ключа из словаря.

my_dict = {'a': 10, 'b': 20, 'c': 5}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Максимальное значение в словаре:", max_value)
print("Минимальное значение в словаре:", min_value)

print("Ключи словаря:")
for key in my_dict:
    print(key)

print("\nЗначения словаря:")
for value in my_dict.values():
    print(value)

my_dict = {'x': list(range(11, 21)), 'y': list(range(21, 31)), 'z': list(range(31, 41))}

print("Словарь с ключами x, y и z и их значениями:")
print(my_dict)

fifth_values = {key: value[4] for key, value in my_dict.items()}

print("Пятые значения каждого ключа в словаре:", fifth_values)



