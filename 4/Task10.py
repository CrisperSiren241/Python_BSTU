names = ["Дмитрий", "Борис", "София", "Давид", "Саша"]
letter = "Д"
filtered_names = filter(lambda name: name.startswith(letter), names)
print(f"Имена, начинающиеся с буквы '{letter}':", list(filtered_names))


