class Organism:
    def __init__(self):
        self.name = ''

    def eat(self, other):
        if other.edible:
            self.fed = True
            self.alive = True
        else:
            self.fed = False
            self.alive = False
        result = str(self.name + ' получил ' + other.name)
        if other.edible:
            result = result + '. ' + self.name + ' съел ' + other.name
        else:
            result = result + '. ' + self.name + ' не стал есть ' + other.name
        if self.fed:
            result = result + '. Насытился. '
        else:
            result = result + '. Остался голоден. '
        if self.alive:
            result = result + 'Жив-здоров!'
        else:
            result = result + 'Умер.'
        return result

class Animal(Organism):

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def about(self):
        print("Привет! Я", self.name)
class Plant(Organism):
    def __init__(self, name):
        self.edible = False
        self.name = name
    def about(self):
        about_str = str('Здравствуйте, я ' + self.name + '. Я из класса ' + self.__class__.__name__.lower()+'. Я ')
        if self.edible:
            pass
        else:
            about_str = about_str + 'не '
        about_str = about_str + 'съедобен.'
        print(about_str)
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    pass

a1 = Predator('Волк')# (Canis lupus L.)')
a1.about()
a2 = Mammal('Слон')# (Elephas maximus L.)')
a2.about()
p1 = Flower('Пион')# (Paeonia officinalis L.)')
p1.about()
p2 = Fruit('Банан')# (Musa paradisiaca L.)')
p2.edible = True
p2.about()
print('-----------------------')
print(a1.eat(p1))
print(a2.eat(p2))