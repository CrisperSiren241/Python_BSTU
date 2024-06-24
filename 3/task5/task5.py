# Напишите программу: 
# для сортировки заданного словаря по ключу; 
# чтобы получить ключ, значение и элемент в словаре; 
# для преобразования строковых значений данного словаря в целочисленные (или числа с плавающей точкой).

my_dict = {'b': 2, 'c': 3, 'a': 1}

sorted_dict = dict(sorted(my_dict.items()))

print("Отсортированный словарь по ключу:", sorted_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Ключ:", key)
    print("Значение:", value)
    print("Элемент в словаре:", (key, value))

    my_dict = {'a': '10', 'b': '20', 'c': '30'}

converted_dict = {key: int(value) for key, value in my_dict.items()}  # Для целочисленных значений
# converted_dict = {key: float(value) for key, value in my_dict.items()}  # Для чисел с плавающей точкой

print("Преобразованный словарь:", converted_dict)


