from math import *

n = int(input("Введите целое число n: "))
squares = [pow(i,2) for i in range(1, n + 1)]
print("Список квадратов чисел от 1 до", n, ":", squares)

