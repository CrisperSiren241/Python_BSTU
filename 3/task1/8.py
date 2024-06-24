input_string = "walk"
if len(input_string) >= 3:
    if input_string.endswith("ing"):
        result = input_string + "ly"
    else:
        result = input_string + "ing"
    print("Результат добавления 'ing' или 'ly':", result)
else:
    print("Результат добавления 'ing' или 'ly':", input_string)
