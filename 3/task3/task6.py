# Дан список чисел. Отсортируйте список, переместив все отрицательные числа в начало списка, а положительные — в конец.
lst = [-5, -3, 8, 1, 6, 4]
neg_nums = sorted([num for num in lst if num < 0], reverse=True)
pos_nums = sorted([num for num in lst if num >= 0])
sorted_lst = neg_nums + pos_nums
print("Задача 6:", sorted_lst)