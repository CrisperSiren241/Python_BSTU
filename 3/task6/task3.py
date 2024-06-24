# Используя множества, вывести различные буквы трёх предложений, то есть такие,какие есть только в одном из них.

sentence1 = "hello world"
sentence2 = "world is beautiful"
sentence3 = "hello python"
unique_letters = set(sentence1) ^ set(sentence2) ^ set(sentence3)
print("Различные буквы трех предложений:", unique_letters)