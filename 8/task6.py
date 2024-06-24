# Создайте класс Animal с атрибутами name и age.
# Определите класс Zoo с атрибутом animals, который будет списком объектов класса Animal.
# Реализуйте методы add_animal() и remove_animal() для добавления и удаления животных из списка.
# Создайте объект класса Zoo и добавьте несколько объектов класса Animal. Затем вызовите методы add_animal() и remove_animal().


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Животное {animal.name} добавлено в зоопарк.")
        else:
            print("Это не животное!")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"Животное {animal.name} удалено из зоопарка.")
        else:
            print("Такого животного нет в зоопарке!")

cat = Animal("Кот", 3)
dog = Animal("Собака", 5)

zoo = Zoo()

zoo.add_animal(cat)
zoo.add_animal(dog)

zoo.remove_animal(cat)
