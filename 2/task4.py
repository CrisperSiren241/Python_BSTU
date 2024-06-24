# Задание 4 (используем for ).
# Используя цикл for выведите  на экран все числа (для каждого - отдельный цикл: всего 7): 
# от 1 до 15
# от 5 до 20
# от 20 до 2
# от 2 до 16 с шагом 2
# от 4 до 44 с шагом 4
# от 5 до 25 с шагом 5
# от 80 до 0 с шагом 10

# Приведите примеры использования:
# for _ in range( V ): pass
# for z, x  in range( V ), range( B ): pass
# for index, fruit in enumerate(fruits): pass
# for name, age in zip(names, ages): pass
# for c else

for num in range(1, 16):
    print(num)
    
print("///")

for num in range(5, 21):
    print(num)

print("///")

for num in range(20, 1, -1):
    print(num)

print("///")

for num in range(2, 17, 2):
    print(num)

print("///")

for num in range(4, 45, 4):
    print(num)

print("///")

for num in range(5, 26, 5):
    print(num)

print("///")

for num in range(80, -1, -10):
    print(num)

print("///")

V = 5
for _ in range(V):
    print("Hello World")

V = 3
B = 4
for z, x in zip(range(V), range(B)):
    print(z, x)

fruits = ['банан', 'манго', 'ананас']
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ['Толя', 'Ваня', 'Леша']
ages = [20, 19, 20]
for name, age in zip(names, ages):
    print(name, age)

for c in range(5):
    print(c)
else:
    print("Все ок")