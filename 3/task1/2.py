sentence = "Анна Антон Бедняк касса"
words = sentence.split()
count = 0
for word in words:
    if 'А' in word or 'а' in word:
        count += 1
print("Количество слов, содержащих хотя бы одну букву 'А':", count)