import os

with open('data.txt', 'w') as file:
    file.write('Lorem ipsum.\n')

os.rename('data.txt', 'datadatadata.txt')

# os.remove('datadatadata.txt')

try:
    with open('datadatadata.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл успешно удален.')
