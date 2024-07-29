from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Вариант с использованием списковой сборки
print([x[0] == x[1] for x in list(zip(first, second))])
# Вариант с использованием lambda-функции
print( list(map(lambda x, y: x == y, first, second)))
print('----------------------------------------')
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a')
        for i in data_set:
            print(i)
            file.write(str(i) + '\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('Во! Получилось!..', ['Ну, ', 'раз уж', 'получилось', chr(44), 'то запишем', 'что-нибудь еще...'])
print('----------------------------------------')
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)
ludoedka_ellotchka = MysticBall('Хамите.','Хо-хо!','Знаменито.','Мрачный.','Мрак.','Жуть.','Парниша.','Не учите меня жить.','Как ребёнка.','Кр-р-расота!','Толстый и красивый.','Поедем на извозчике.','Поедем на таксо.','У вас вся спина белая.','Подумаешь!','Ого!')
# Людоедка-Эллочка - второстепенная героиня сатирического романа Ильи Ильфа и Евгения Петрова «Двенадцать стульев»
# Образ стал нарицательным. В переносном смысле — человек со скудным, вульгарным словарным запасом.
# Использованный набор слов соответствует роману.
print(ludoedka_ellotchka())
print(ludoedka_ellotchka())
print(ludoedka_ellotchka())