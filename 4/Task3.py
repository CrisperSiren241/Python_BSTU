# Описать функцию PerfectNumber, определяющую, является ли заданное положительное число совершенным числом. Совершенным числом называется число, равное сумме своих делителей (кроме самого числа).


def PerfectNumber(n):
    if n <= 0:
        return False
    sum_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_divisors == n

number = 27
if PerfectNumber(number):
    print(number, "является совершенным числом.")
else:
    print(number, "не является совершенным числом.")

    