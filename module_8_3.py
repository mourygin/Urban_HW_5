class Car():
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        if not isinstance(__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif __vin < 1000000 or __vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        #print(exc.message)
        self.__numbers = __numbers
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        #print(exc.message)
    def __is_valid_vin(vin_number):
        pass
    def __is_valid_numbers(numbers):
        pass

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers (Exception):
    def __init__(self, message):
        self.message = message



if __name__ == '__main__':
    try:
        first = Car('Model1', '10000000', 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        first = Car('Model3', 10000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model4', 5555555, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model5', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        forth = Car('Model5', 2020202, 'abc')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        fifth = Car('Model6', 2020202, ['f123dj'])
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')