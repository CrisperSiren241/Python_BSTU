# Дана целочисленная матрица размера M × N. 
# Найти номер первого из ее столбцов,содержащих только нечетные числа. Если таких столбцов нет, то вывести 0.
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
m, n = len(matrix), len(matrix[0])
for j in range(n):
    column = [matrix[i][j] for i in range(m)]
    if all(num % 2 != 0 for num in column):
        print("Задача 7:", j + 1)
        break
else:
    print("Задача 7:", 0)