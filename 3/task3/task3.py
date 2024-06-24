# Дан список. Найти количество пар элементов списка, которые являются взаимно противоположными.
lst = [1, -1, 2, -2, 3, -3]
count = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == -lst[j]:
            count += 1
print("Задача 3:", count)