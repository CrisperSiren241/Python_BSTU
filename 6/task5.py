from datetime import datetime

def find_spring_dates(filename):
    spring_dates = []
    with open(filename, 'r') as file:
        for line in file:
            date = datetime.strptime(line.strip(), '%d-%m-%Y')
            if 3 <= date.month <= 5:
                spring_dates.append(date)
    return spring_dates

def filter_numbers(file_f, file_g):
    with open(file_f, 'r') as f, open(file_g, 'w') as g:
        for line in f:
            number = int(line.strip())
            if number % 3 == 0 and number % 7 != 0:
                g.write(str(number) + '\n')

def min_even_indexed_number(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    return min(numbers[i] for i in range(0, len(numbers), 2))

def split_even_odd(file_f, file_g, file_h):
    with open(file_f, 'r') as f, open(file_g, 'w') as g, open(file_h, 'w') as h:
        for line in f:
            numbers = line.strip().split()
            for number in numbers:
                number = int(number)
                if number % 2 == 0:
                    g.write(str(number) + ' ')
                else:
                    h.write(str(number) + ' ')
            g.write('\n')
            h.write('\n')

# print(find_spring_dates("task5_1.txt"))
# filter_numbers("task5_2_1.txt", "task5_2_2.txt")
# min_even_indexed_number("task5_3.txt")
split_even_odd("task5_4_1.txt", "task5_4_2.txt", "task5_4_3.txt")