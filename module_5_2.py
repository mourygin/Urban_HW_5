class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.hystorical_building = False

    def go_to(self, new_floor):
        global number_of_floors
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(new_floor,' - Такого этажа не существует')

    def where_we_are(self):
        print(f'Сейчас мы находимся в здании "{self.name}"')

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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Зимний дворец', 3)
h3.hystorical_building = True
h1.where_we_are()
h1.set_new_number_of_floors(20)
print()
h2.where_we_are()
h2.set_new_number_of_floors(1)
print()
h3.where_we_are()
h3.set_new_number_of_floors(4)