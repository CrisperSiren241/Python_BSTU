import os

N = int(input("Сколько папок надо создать? "))

for i in range(1, N+1):
    os.makedirs(f'folder/folder{i}')

os.rmdir('folder/folder2')
os.rmdir('folder/folder4')
