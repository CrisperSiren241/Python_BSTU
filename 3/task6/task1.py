# Дана непустая последовательность символов. Построить и напечатать множества,элементами которых являются встречающиеся в последовательности: 
# а) цифры от«0» до «9» и знаки арифметических операций; 
# б) буквы от «A» до «F» и от «X»до «Z».

# а) Множество цифр от «0» до «9» и знаков арифметических операций
sequence = "a1b2c+3-4*5"
digits_and_operators = {char for char in sequence if char.isdigit() or char in {'+', '-', '*'}}
print("Множество цифр и знаков операций:", digits_and_operators)

# б) Множество букв от «A» до «F» и от «X» до «Z»
sequence = "aAbBcCXxYyZz"
letters_A_to_F_X_to_Z = {char for char in sequence if char.isalpha() and ('A' <= char <= 'F' or 'X' <= char <= 'Z')}
print("Множество букв A-F и X-Z:", letters_A_to_F_X_to_Z)

