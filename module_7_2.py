def custom_write(file_name, strings):
    file = open(file_name, 'w')
    res_dict = {}
    line_nr = 1
    for i in strings:
        start_pos = file.tell()
        file.write(i + '\n')
        key = (line_nr, start_pos)
        res_dict[key] = i
        line_nr += 1
    return res_dict

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)