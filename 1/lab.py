from math import *
from time import *
# Задание 1.
# Для ввода информации в переменные используется input(), для вывода - print().
# Используя эти команды создайте 5 переменных и введите с клавиатуры в них значения различных типов (целый, вещественный, логический, строка).
# При помощи type() выведите типы этих переменных на экран.
# Создайте ещё 5 переменных, но при их записи используйте команды для преобразования данных в нужный тип. Выведите их на экран вместе с их типом.

# a = input("enter int = ")
# b = input("enter float = ")
# c = input("enter bool = ")
# e = input("enter string = ")

# print(type(a), type(b), type(c), type(e))

# a = int(input("enter int = "))
# b = float(input("enter float = "))
# c = bool(input("enter bool = "))
# e = input("enter string = ")

# print(type(a), type(b), type(c), type(e))

#Создайте ещё 5 переменных, которые используют переменные a, b, c для вычисления суммы, разности, произведения, остатка от деления, деления без остатка.

# a, b, c = 10, 2, 7

# sum = a + b + c
# diff = a - b - c
# multi = a * b * c
# mlt1 = a % b 
# mlt2 = a % c
# dele = a/b; 
# print("\n", f"Сумма = {sum} \n",
#       f"Разность = {diff} \n",
#       f"Произведение = {multi} \n",
#       f"Остаток от деления 1 = {mlt1} \n",
#       f"Остаток от деления 2 = {mlt2} \n",
#       f"Деление без остатка = {dele} \n")


# a, b = b, a
# print(f"a = {a} \n"
#       f"b = {b}")


print(
    ((int(x:=input("x = "))**2 + 12 * int(c:= input("c = ")) - sqrt(int(x))) / (4*int(v:=input("v = ")))) - int(x)**4,
       
    (sin(2*int(b:=input("b = ")))+sqrt(3*int(c))-44*cos(4*int(x))), 

    (int(x) % 2 + int(c)//4 - int(v)//10 + 18*int(b)), 
      
      sep="**-**", end="!!!")

# print(math.sin(2*int(input("b = ")))+math.sqrt(3*int(input("v = ")))-44*math.cos(4*int(input("x = "))))

# print(int(input("x = ")) % 2 + int(input("c = "))//4 - int(input("v = "))//10 + 18*int(input("b = ")))

# name = input("Твое имя? = ")
# age = input("Твой возраст? = ")

# print("Привет {}! Тебе {} лет".format(name, age))

# rad = float(input("Радиус окружности? = "))
# s = pi*rad**2

# print("Площадь окружности радиусом {} равна {} ".format(rad, s))

# a = int(input("a = "))
# b = int(input("b = "))

# del1 = a / b
# del2 = b / a

# print("Первое вычисление {:.3f}, Второе вычисление {:.2f}".format(del1, del2))

current_time = time()
local_time = localtime(current_time)
 
formatted_time = strftime("%Y-%m-%d %H:%M:%S", local_time)
formatted_time1 = strftime("%H:%M:%S", local_time)
formatted_time2 = strftime("%d/%m/%Y", local_time)

formatted_time3 = strftime("%Y.%m.%d %H:%M:%S", local_time)
formatted_time4 = strftime("%H:%M", local_time)
formatted_time5 = strftime("%d %B %Y", local_time)

print("\n", "Текущие дата и время", formatted_time)
print("Текущее время", formatted_time1)
print("Текущая дата", formatted_time2, "\n")

print("Текущие дата и время", formatted_time3)
print("Текущее время", formatted_time4)
print("Текущая дата", formatted_time5)
