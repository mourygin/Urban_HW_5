import random
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        #self.__color = __COLOR_VARIANTS[randint(0, 4)]
        if __color in Vehicle.__COLOR_VARIANTS:
            self.__color = __color
        else:
            self.__color = 'white'
            print('Применен цвет по умолчанию - white')
    def get_model(self):
        return 'Модель: ' + self.__model
    def get_horsepower(self):
        return 'Мощность двигателя: ' + str(self.__engine_power)
    def get_color(self):
        return 'Цвет: ' + self.__color
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)
    def set_color(self, new_color):
        if str(new_color).lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = str(new_color).lower()
        else:
            print('Нельзя сменить цвет на', new_color)
    def set_engine(self, new_engine):
        self.__engine_power = new_engine

class Sedan(Vehicle):
    # def __init__(self, owner, __model, __engine_power, __color):
    __PASSENGERS_LIMIT = 5

#tachka1 = Vehicle('Vasia', 'Renault Sandero', 75, 'pink')
tachka1 = Sedan('Vasia', 'Renault Sandero', 75, 'red')
tachka1.print_info()
print('-----------Перекраска 1...-----------')
tachka1.__color = 'black'
tachka1.print_info()
print('-----------Перекраска 2...-----------')
tachka1.set_color('pink')
tachka1.print_info()
print('-----------Перекраска 3...-----------')
tachka1.set_color('GREEN')
tachka1.print_info()
print('--- Самому покрасить не удалось. Придется ездить на зеленой... ----')
print('-----------Смена двигателя 1...-----------')
tachka1.__engine_power = 120
tachka1.print_info()
print('--- Не вышло. Ладно хоть не сломал ничего. На сервис! ----')
print('-----------Смена двигателя 2...-----------')
tachka1.set_engine(90)
tachka1.print_info()

