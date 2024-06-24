# Описать рекурсивные функции Fact и Fact2, вычисляющие значения факториала N!и двойного факториала N!! соответственно (N > 0 — параметр целого типа).


def Fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Fact(n - 1)

def Fact2(n):
    if n <= 0:
        return 1
    else:
        return n * Fact2(n - 2)

N = 5
print(f"Факториал {N}: {Fact(N)}")
print(f"Двойной факториал {N}: {Fact2(N)}")


