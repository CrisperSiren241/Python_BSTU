# Дан список. Найти произведение всех элементов списка, 
# расположенных между его минимальным и максимальным элементами, включая минимальный и максимальный элементы.
lst = [1, 3, 2, 4, 6, 5]
min_index = lst.index(min(lst))
max_index = lst.index(max(lst))
start = min(min_index, max_index)
end = max(min_index, max_index)
result = 1
for num in lst[start:end+1]:
    result *= num
print("Задача 2:", result)