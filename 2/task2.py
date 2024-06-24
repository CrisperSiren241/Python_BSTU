import math
# Написать мини-калькулятор. 
# Необходимо спросить какую операцию необходимо сделать :  /, *,-,+,//, **, sin, cos, tg, корень. Далее в зависимости от выбранной операции попросить ввести одно или два числа. После этого посчитать результат и вывести его.

operation = input("Введите операцию /, *,-,+,//, **, sin, cos, tg, корень = ")

match operation:
    case "/":
        a = int(input("a = "))
        b = int(input("b = "))
        print(f"Результат = {a/b}")
    case "*": 
        a = int(input("a = "))
        b = int(input("b = "))
        print(f"Результат = {a*b}")
    case "-":
        a = int(input("a = "))
        b = int(input("b = "))
        print(f"Результат = {a-b}")
    case "+":
        a = int(input("a = "))
        b = int(input("b = "))
        print(f"Результат = {a+b}")
    case "//":
        a = int(input("a = "))
        b = int(input("b = "))
        print(f"Результат = {a//b}")
    case "**":
        a = int(input("a(Число) = "))
        b = int(input("b(степень) = "))
        print(f"Результат = {a**b}")
    case "sin":
        a = int(input("a = "))
        print(f"Результат = {math.sin(math.radians(a))}")
    case "cos":
        a = int(input("a = "))
        print(f"Результат = {math.cos(math.radians(a))}")
    case "tg":
        a = int(input("a = "))
        print(f"Результат = {math.tan(math.radians(a))}")
    case "корень":
        a = int(input("a = "))
        print(f"Результат = {math.sqrt(a)}") 
