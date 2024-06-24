# Описать функцию RemoveRowCol, удаляющую из матрицы A размера M × N строкуи столбец, которые содержат элемент AK, L (предполагается, что M > 1 и N > 1; еслиK > M или L > N, то матрица не изменяется).


def RemoveRowCol(matrix, K, L):
    if K > len(matrix) or L > len(matrix[0]) or K <= 0 or L <= 0:
        return matrix
    return [row[:L-1] + row[L:] for row in (matrix[:K-1] + matrix[K:])]

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
K = 2
L = 2
new_matrix = RemoveRowCol(A, K, L)
for row in new_matrix:
    print(row)


