# Напишите программу, которая просит ввести с клавиатуры  число X с клавиатуры, исходя из введенного число выведите последовательность следующую последовательность (от 0 до 10): 0, 1*X, 2*X, …,  10*X.

x = 0
a = int(input("a = "))

while x <= 10:
    print(f"{x*a}")
    x += 1 