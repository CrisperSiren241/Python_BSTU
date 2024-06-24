import random

names = ["Анна", "Петр", "Елена", "Иван", "Мария"]
random_name = random.choice(names)

print("Случайное имя из списка: ", random_name)

import calculator

sum = calculator.add(364, 679)
difference = calculator.subtract(23, 75)
product = calculator.multiply(47, 2)
division = calculator.divide(35, 5)

print("Сумма: ", sum)
print("Разность: ", difference)
print("Произведение: ", product)
print("Деление: ", division)

import lists

random_list = lists.randomList(10)
random_matrix = lists.randomMatrix(3)
words = ['яблоко', 'банан', 'апельсин', 'клубника', 'киви']
numbers = [1, 4, 6, 9, 2, 5]

print("Случайный список:", random_list)
print("Случайная матрица:")
for row in random_matrix:
    print(row)
print("Самое длинное слово в списке:", lists.maxLength(words))
print("Новый список с суммами элементов:", lists.currentSums(numbers))
print("Список из трех символов:", lists.threeSimbol("Hello, World!"))