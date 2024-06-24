# Создаем пустой список
shopping_list = []

# Запрашиваем у пользователя ввод элементов списка покупок
while True:
    item = input("Введите элемент списка покупок или 'готово' для завершения: ")
    if item.lower() == 'готово':
        break
    shopping_list.append(item)

# Выводим список покупок
print("Ваш список покупок: ", shopping_list)

# Проверяем, пуст ли список
if not shopping_list:
    print("Список покупок пуст!")
else:
    # Предлагаем пользователю обновить элемент списка
    index = int(input("Введите индекс элемента, который вы хотите обновить: "))
    new_value = input("Введите новое значение для этого элемента: ")
    shopping_list[index] = new_value

    # Предлагаем пользователю удалить элемент списка
    item_to_remove = input("Введите элемент списка, который вы хотите удалить: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Ошибка: этого элемента нет в списке покупок.")

    # Сортируем список покупок
    shopping_list = sorted(shopping_list)

    # Выводим отсортированный список
    print("Ваш отсортированный список покупок: ")
    for item in shopping_list:
        print(item)

    # Подсчитываем количество элементов в списке
    print("Количество элементов в списке покупок: ", len(shopping_list))
