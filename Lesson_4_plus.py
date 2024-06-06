import datetime
current_year = datetime.date.today().year
name = input("Введите Ваше имя: ")
print('Здравствуйте,', name + '.')
date_of_birth = ''
while not (date_of_birth.isnumeric()):
    date_of_birth = input('В каком году Вы родились? ')
date_of_birth = int(date_of_birth)
age = current_year - date_of_birth
if ((abs(age) % 10 == 1) and (abs(age) % 100 != 11)):
    years = 'год'
elif ((abs(age) % 10 < 0) and (abs(age) % 10 < 5) and (abs(age) % 100 != 11)):
    years = 'года'
else:
    years = 'лет'
if age > 0:
    print('В этом году Вам ', age, years)
elif age == 0:
    print('Еще и года нет?! Подрастай малыш! Когда вырастешь приходи учиться в Urban University.')
else:
    print('Вы, кажется, еще не родились. Придется подождать еще', age * (-1), years)