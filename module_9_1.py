def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        f = i(int_list)
        result[i.__name__] = f
    return result


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))