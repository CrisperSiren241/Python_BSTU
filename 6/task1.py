with open('example.txt', 'w') as file:
    file.write('first\n')
    file.write('Second\n')

with open(f'example.txt', 'r') as file:
    print(file.read())
