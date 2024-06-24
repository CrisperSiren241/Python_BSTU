# Используя множества, напечатать по одному разу в алфавитном порядке все строчные русские гласные буквы, входящие в заданный текст.

text = "Привет, как дела?"
vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
russian_vowels_in_text = sorted(set(char.lower() for char in text if char.lower() in vowels))
print("Строчные русские гласные буквы в тексте:", russian_vowels_in_text)
