def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:

                result += i
                #print(result, i)
            except TypeError:
                print('Некорректный тип данных для подсчёта суммы -', i)
                incorrect_data += 1
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
        return (None, None)
    a = (result, incorrect_data)
    return a
def calculate_average(numbers):
    b = personal_sum(numbers)
    try:
        avr = b[0] / (len(numbers) - b[1])
    except TypeError as exc:
        return None
    except ZeroDivisionError as exc:
        avr = 0
    return avr
if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать