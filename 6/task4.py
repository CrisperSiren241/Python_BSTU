# Дано целое число K (0 < K < 10) и текстовый файл, содержащий более K строк.Удалить из файла последние K строк.

def remove_last_k_lines(filename, k):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        file.writelines(lines[:-k])

# Дано целое число K и текстовый файл. Удалить из каждой строки файла первые K Символов (если длина строки меньше K, то удалить из нее все символы).

def remove_first_k_chars(filename, k):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line[k:] if len(line) > k else '\n')

# Даны два текстовых файла. Добавить в конец каждой строки первого файла соответствующую строку второго файла. Если второй файл короче первого, то остав-шиеся строки первого файла не изменять.

def append_file_to_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    with open(file1, 'w') as f1:
        for i, line in enumerate(lines1):
            f1.write(line.rstrip('\n') + (lines2[i] if i < len(lines2) else '') + '\n')

# Дано целое число K и текстовый файл. Удалить из файла строку с номером K. Если Строки с таким номером нет, то оставить файл без изменений.

def remove_line_k(filename, k):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for i, line in enumerate(lines):
            if i != k-1:
                file.write(line)

import string

def create_punctuation_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
    with open(output_file, 'w') as file:
        for char in text:
            if char in string.punctuation:
                file.write(char)


def count_and_sum_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    numbers = [int(line.strip()) for line in lines]
    print(f'Количество чисел: {len(numbers)}')
    print(f'Сумма чисел: {sum(numbers)}')

remove_last_k_lines("task4_1.txt", 4)
remove_first_k_chars("task4_2.txt", 4)
append_file_to_file("task4_3_1.txt", "task4_3_2.txt")
remove_line_k("task4_4.txt", 2)
create_punctuation_file("task4_5.txt", "data3.txt")
count_and_sum_numbers("task4_6.txt")