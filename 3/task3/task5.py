# Дан список. Выбрать из списка все отрицательные числа и упорядочить их по возрастанию.
lst = [5, -3, 8, -1, 6, -4]
filtered_lst = sorted([num for num in lst if num < 0])
print("Задача 5:", filtered_lst)