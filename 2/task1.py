import math

H = 3.02  # исходная энтропия
p_values = [0.1, 0.5, 1]  # вероятности ошибок

for p in p_values:
    H_eff = H - math.log2(1/p)
    print(f'Эффективная энтропия при p={p} равна {H_eff} бит.')
