# Создайте класс Person с закрытыми атрибутами name и age.
# Определите методы get_name(), set_name(), get_age() и set_age(), чтобы получить и установить значения атрибутов.
# Создайте объект класса Person и используйте методы для получения и установки значений атрибутов.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Создание объекта класса Person
person = Person("Иван", 30)

# Использование методов для получения и установки значений атрибутов
print(person.get_name())  # Выводит: Иван
print(person.get_age())   # Выводит: 30

person.set_name("Алексей")
person.set_age(35)

print(person.get_name())  # Выводит: Алексей
print(person.get_age())   # Выводит: 35
