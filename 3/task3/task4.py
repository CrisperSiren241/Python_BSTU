# Дан список. Выбрать из списка все числа больше заданного числа k и упорядочить их по убыванию.
lst = [5, 3, 8, 1, 6, 4]
k = 3
filtered_lst = sorted([num for num in lst if num > k], reverse=True)
print("Задача 4:", filtered_lst)