# Дана матрица размера M × N. Найти номер ее строки с наибольшей суммой элементов и вывести данный номер, а также значение наибольшей суммы.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max_sum = float('-inf')
max_sum_row = -1 

for i in range(len(matrix)):
    row_sum = sum(matrix[i]) 
    if row_sum > max_sum:
        max_sum = row_sum
        max_sum_row = i

print("Номер строки с наибольшей суммой элементов:", max_sum_row + 1)
print("Значение наибольшей суммы:", max_sum)