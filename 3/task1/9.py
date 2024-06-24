input_string = "Hop Hey lala-lei"
encrypted_sentence = ""
for char in input_string:
    if char.isalpha():
        if char.islower():
            encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        encrypted_char = char
    encrypted_sentence += encrypted_char
print("Зашифрованная строка:", encrypted_sentence)
