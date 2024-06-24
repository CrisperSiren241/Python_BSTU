sentence = "Программа"
even_chars = sentence[::2]
odd_chars = sentence[1::2]
encrypted_sentence = even_chars + odd_chars[::-1]
print("Зашифрованная строка:", encrypted_sentence)