input_string = "banana banana"
if len(input_string) >= 2:
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    print("Результат замены первого символа:", modified_string)
else:
    print("Результат замены первого символа:", input_string)
