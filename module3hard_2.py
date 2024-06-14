def x_function(xx_string):
    x_string = str(xx_string)
    if x_string == '()':
        return ''
    opener = 0
    while opener >= 0:
        opener = str(x_string).find("(", 0)
        if opener == -1:
            return x_string
        closer = find_closer(x_string, opener)
        x_string = x_string[0:opener] + x_function(x_string[opener + 1:closer]) + x_string[closer + 1:]

def find_closer(string_, opener_pos):
    level = -1

    for i in range(opener_pos,len(string_)): # Пробегаем по строке пока не найдем

        if string_[i] == '(':
            level += 1
        elif string_[i] == ')' and level == 0:
            return i
        elif string_[i] == ')' and level > 0:
            level -= 1
        else:
            pass
        #print(i, string_[i], level)
##################################################
frag_code = """data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]"""
# Возьмем правую часть строки без пробелов и переносов

string_code = ''
components = []
for i in frag_code:
    if ord(i) != 10 and i != ' ':
        string_code = string_code + i
string_code = string_code[string_code.find('=') + 1:]
# Унифицируем скобки. Все переведем как-бы в "кортежи", хотя это пока просто строка.
tmp_1 = string_code.replace('[', '(')
tmp_2 = tmp_1.replace(']', ')')
tmp_1 = tmp_2.replace('{', '(')
tmp_2 = tmp_1.replace('}', ')')
tmp_1 = tmp_2.replace(':', ',')
string_code = tmp_1

# Ищем строки и замещаем их количеством символов
beg = 0
while True:
    d_open = string_code.find("'", beg)
    if d_open > -1:
        d_close = string_code.find("'", d_open + 1)
        tmp_1 = string_code[0:d_open] + str(d_close - d_open - 1) + string_code[d_close + 1:]
        string_code = tmp_1
    else:
        break
beg = 0
while True:
    d_open = string_code.find('"', beg)
    if d_open > -1:
        d_close = string_code.find('"', d_open + 1)
        tmp_1 = string_code[0:d_open] + str(d_close - d_open - 1) + string_code[d_close + 1:]
        string_code = tmp_1
    else:
        break

# Отладочная строка
#string_code = str("9,8,7,('a','b','c',('X', 'Y', 'Z')),6,(1,2,2),5,4")

result = x_function(string_code)
list_ =list(result.split(','))
total = 0
for i in list_:
    if type(i) == 'str':
        total += len(i)
    elif i.isnumeric():
        total += int(i)

print('Result is',total)