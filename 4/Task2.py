# Создайте функцию merge_strings, которая принимает две строки в качестве аргументов.
# Внутри функции объедините две строки в одну и верните полученную строку.
# Протестируйте функцию, передавая различные строки, и выведите результат на экран


def merge_strings(str1, str2):
    return str1 + str2

string1 = "Hello, "
string2 = "world!"
print("Объединенная строка:", merge_strings(string1, string2))

string3 = "Яблоки "
string4 = "и груши"
print("Объединенная строка:", merge_strings(string3, string4))

