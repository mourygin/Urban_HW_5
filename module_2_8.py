def get_multiplied_digits (number):
    str_number = str(number)
    while True:
        str_first = str_number[:1]
        if str_first == '0':
            str_number = str_number[1:]
            continue
        else:
            first = int(str_number[:1])
            break
    if len(str_number) > 1:
        return first * get_multiplied_digits(str_number[1:])
    else:
        return first


print(get_multiplied_digits('402000103'))