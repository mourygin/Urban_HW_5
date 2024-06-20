class House:
    total = 0

    def __init__(self, name, number_of_floors, building_type, flats_on_floor):
        self.name = name
        self.number_of_floors = number_of_floors
        self.hystorical_building = False
        self.building_type = building_type
        self.flats_on_floor = 0 # Количество квартир на этаже. 0 - без деления на квартиры.
        if building_type not in ['Сборный ж/б', 'Монолит ж/б', 'Кирпичная кладка', 'Бревенчатый сруб', 'Каркас утепленный']:
            building_type = 'Unknown'
        House.total += 1

    def __eq__(self, other):
        if type(self) == type(other):
            # a1 = self.number_of_floors == other.number_of_floors
            # a2 = (self.number_of_floors * self.flats_on_floor) == (other.number_of_floors * other.flats_on_floor)
            # return tuple(a1,a2)
            return (self.number_of_floors == other.number_of_floors) and ((self.number_of_floors * self.flats_on_floor) == (other.number_of_floors * other.flats_on_floor))

    def where_we_are(self):
        msg = f'Сейчас мы находимся в здании "{self.name}". ({self.building_type}. {self.number_of_floors} эт., '
        if self.flats_on_floor == 0:
            msg += 'Единое здание.)'
        else:
            msg += f'{self.number_of_floors * self.flats_on_floor} кв.)'
        print(msg)

    def set_new_number_of_floors(self, floors):
        #global number_of_floors, hystorical_building
        if floors < self.number_of_floors:
            print('Нельзя удалять уже построенные этажи. Их можно только надстраивать.')
        else:
            if self.hystorical_building:
                print('Запрещена перестройка исторических зданий.')
            else:
                added_flores = floors - self.number_of_floors
                self.number_of_floors = floors
                print(f'К зданию "{self.name}" было надстроено {added_flores} этаж/а/ей.')

import random

vilage_pythonovo = []
technology = ['Сборный ж/б', 'Монолит ж/б', 'Кирпичная кладка', 'Бревенчатый сруб', 'Каркас утепленный']
for i in range(40):
    new_house = House(chr(65 + random.randint(0,25)) + chr(65 + random.randint(0,25)), random.randint(1, 3), technology[random.randint(0,4)],0)
    vilage_pythonovo.append(new_house)
print(f'В деревне Питоново было построено {House.total} домов различной этажности и конструкции.')
print('------------------------------------------------')
for i in vilage_pythonovo:
    print(i.name, i.number_of_floors, i.building_type)