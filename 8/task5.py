# Создайте класс Engine с методом start(), который выводит сообщение о запуске двигателя.
# Создайте класс Car с атрибутом engine, который будет экземпляром класса Engine.
# Определите метод start_engine(), который будет вызывать метод start() у объекта engine.
# Создайте объект класса Car и вызовите метод start_engine().


class Engine:
    def start(self):
        return "Двигатель запущен"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        return self.engine.start()

# Создание объекта класса Car
car = Car()

# Вызов метода start_engine()
print(car.start_engine())  # Выводит: Двигатель запущен
