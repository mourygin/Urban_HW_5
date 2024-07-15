def count_calls():
    global calls
    calls += 1
    return

def string_info(string):
    str_len = len(string)
    str_up = str(string).upper()
    str_dn = str(string).lower()
    result = tuple((str_len, str_up, str_dn))
    count_calls()
    return result

def is_contains(string, list_to_search):
    result = False
    for i in list_to_search:
        if str(string).upper() == str(i).upper():
            result = True
    count_calls()
    return result
if __name__ == '__main__':
    calls = 0
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
    print(calls)