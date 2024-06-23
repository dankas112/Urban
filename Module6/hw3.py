class Vehicle:
    __COLOR_VARIANTS = ('red', 'blue', 'green', 'white', 'black')
    vehicle_type = 'none'

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Car:
    price = 1000000

    def horse_powers(self):
        super().get_horsepower()


class Nissan(Car, Vehicle):
    price = 250000
    vehicle_type = 'Car'

    def horse_powers(self):
        super().horse_powers()


# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# vehicle1.print_info()
# print(Sedan.mro())

vehicle2 = Nissan('Pedro', 'Toyota Mark II', 'blue', 500)
print(vehicle2.price, vehicle2.vehicle_type)
vehicle2.horse_powers()
