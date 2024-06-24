input_string = "hello world"
capitalized_string = ' '.join(word.capitalize() for word in input_string.split())
capitalized_string = ''.join(sorted(set(input_string), key=input_string.index))
print("Результат удаления дубликатов:", capitalized_string)
