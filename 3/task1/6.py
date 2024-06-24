import os
file_path = "D:\\BSTU\\primer\\prog.py"
filename_without_extension = os.path.splitext(os.path.basename(file_path))[0]
print("Имя файла без расширения:", filename_without_extension)