# Создайте класс Animal с методом make_sound().
# Определите классы Dog, Cat и Cow, которые наследуются от Animal.
# В каждом из этих классов переопределите метод make_sound(), чтобы он возвращал соответствующий звук животного.
# Создайте список объектов разных типов (например, Dog, Cat и Cow) и вызовите для каждого объекта метод make_sound().

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав"

class Cat(Animal):
    def make_sound(self):
        return "Мяу"

class Cow(Animal):
    def make_sound(self):
        return "Муу"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())
