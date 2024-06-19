class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        global number_of_floors
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(new_floor,' - Такого этажа не существует')

    def where_we_are(self):
        print(f'Сейчас мы находимся в здании "{self.name}"')




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Зимний дворец', 3)
h1.where_we_are()
h1.go_to(5)
h2.where_we_are()
h2.go_to(10)
h3.where_we_are()
h3.go_to(3)