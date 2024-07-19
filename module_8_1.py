'''
Написал функцию в двух вариантах, add_everything_up и add_everything_up_2. Второй вариант мне нравится больше,
но у него есть один небольшой недостаток. Это отсутствие оператора Try. 
'''
def similar_to(a, b):
    if b.__class__.__name__ == 'int':
        a = int(a)
        return a
    elif b.__class__.__name__ == 'float':
        a = float(a)
        return a
    elif b.__class__.__name__ == 'str':
        a = str(a)
        return a

def add_everything_up(a, b):
    if type(a) == type(b):
        return a + b
    else:
        try:
            b = similar_to(b,a)
        except:
            a = similar_to(a,b)
        return a + b

def add_everything_up_2(a, b):
    dict = {('int', 'int'): 'int', ('int', 'float'): 'float', ('int', 'str'): 'str',
            ('float', 'float'): 'float', ('float', 'int'): 'float', ('float', 'str'): 'str',
            ('str', 'int'): 'str', ('str', 'float'): 'str', ('str', 'str'): 'str'}
    type_ = dict[(a.__class__.__name__, b.__class__.__name__)]
    if type_ == 'int':
        a = int(a)
        b = int(b)
    if type_ == 'float':
        a = float(a)
        b = float(b)
    if type_ == 'str':
        a = str(a)
        b = str(b)
    return a + b

if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    print('--------------------------------')
    print(add_everything_up_2(123.456, 'строка'))
    print(add_everything_up_2('яблоко', 4215))
    print(add_everything_up_2(123.456, 7))