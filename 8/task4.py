# Создайте класс Place с атрибутами area и address и методом to_sell(), который выводит сообщение о продаже данной недвижимости с указанием площади и адреса.
# Определите класс Apartment , который наследуется от Place и добавляет атрибут rooms.
# Определите класс House, который также наследуется от Place и добавляет атрибут floors.
# Создайте объекты Apartment и House и вызовите их методы.


class Place:
    def __init__(self, area, address):
        self.area = area
        self.address = address

    def to_sell(self):
        return f"Продается недвижимость по адресу {self.address} площадью {self.area} кв. м."

class Apartment(Place):
    def __init__(self, area, address, rooms):
        super().__init__(area, address)
        self.rooms = rooms

class House(Place):
    def __init__(self, area, address, floors):
        super().__init__(area, address)
        self.floors = floors

apartment = Apartment(100, "ул. Пушкина, д. 10", 3)
house = House(200, "ул. Ленина, д. 20", 2)

print(apartment.to_sell())  
print(house.to_sell())
