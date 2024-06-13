frag_code = """data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]"""
deviders = ['[', ']', '(', ')', '{', '}']
# Возьмем правую часть строки без пробелов и переносов

string_code = ''
components = []
for i in frag_code:
    if ord(i) != 10 and i != ' ':
        string_code = string_code + i
string_code = string_code[string_code.find('=') + 1:]
for i in string_code:
    if i not in deviders:
        components.append(i)
print(string_code)
tmp_1 = string_code.replace('(','')
tmp_2 = tmp_1.replace(')','')
tmp_1 = tmp_2.replace('[','')
tmp_2 = tmp_1.replace(']','')
tmp_1 = tmp_2.replace('{','')
tmp_2 = tmp_1.replace('}','')
tmp_1 = tmp_2.replace(':',',')
tmp_2 = tmp_1.replace("'",'')
tmp_1 = tmp_2.replace('"','')
new_list = tuple(tmp_1.split(','))
result = 0
for i in new_list:
    if i.isnumeric():
        result += int(i)
    else:
        result += len(i)
print(result)
