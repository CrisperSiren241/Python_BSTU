# Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
for i in range(len(matrix)):
    min_index = matrix[i].index(min(matrix[i]))
    max_index = matrix[i].index(max(matrix[i]))
    matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]
print("Задача 8:")
for row in matrix:
    print(row)