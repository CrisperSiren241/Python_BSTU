# Даны три строки. Используя множества, определить, можно ли из символов первых двух строк получить третью строку.

string1 = "abc"
string2 = "def"
string3 = "abcdef"
can_be_constructed = set(string3) == set(string1) | set(string2)
print("Можно ли из символов первых двух строк получить третью строку:", can_be_constructed)
