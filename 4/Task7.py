# Создайте функцию print_user_info, которая принимает три аргумента: name типа str, age типа int и city типа str (	по умолчанию - Минск).
# Внутри функции выведите информацию о пользователе в формате "Имя: [name], Возраст: [age], Город: [city]".
# Протестируйте функцию, передавая различные значения для аргументов, и выведите результат на экран.


def print_user_info(name, age, city="Минск"):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

print_user_info("Мария", 20, "Москва")
print_user_info("Анна", 26)

