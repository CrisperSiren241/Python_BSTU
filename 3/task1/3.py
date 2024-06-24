sentence = "Аннарасуманара тот тета-тет"
words = sentence.split()
shortest_length = min(len(word) for word in words)
print("Длина самого короткого слова:", shortest_length)