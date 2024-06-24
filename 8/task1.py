# Создайте абстрактный класс Shape с методом calculate_area().
# Определите два класса, Circle и Rectangle, которые наследуются от Shape.
# В каждом из этих классов реализуйте метод calculate_area(), чтобы он возвращал площадь соответствующей фигуры.
# Создайте объекты Circle и Rectangle и вызовите их методы calculate_area().

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Создание объектов
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Вызов методов
print(f"Площадь круга: {circle.calculate_area()}")
print(f"Площадь прямоугольника: {rectangle.calculate_area()}")
