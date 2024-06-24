# Описать функцию FlattenList, которая принимает вложенный список и возвращает одноуровневый список, содержащий все элементы из вложенных списков.


def FlattenList(nested_list):
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(FlattenList(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9, 10]]]
print("Одноуровневый список:", FlattenList(nested_list))

