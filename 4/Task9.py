# Создайте список numbers, содержащий несколько целых чисел. Используя lambda-выражение, отсортируйте список в порядке возрастания или убывания. 
# Выведите отсортированный список на экран.


numbers = [5, 2, 8, 1, 9]
sorted_asc = sorted(numbers, key=lambda x: x)
sorted_desc = sorted(numbers, key=lambda x: -x)
print("Отсортированный список по возрастанию:", sorted_asc)
print("Отсортированный список по убыванию:", sorted_desc)


