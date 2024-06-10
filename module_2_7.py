def print_params(a = 1, b = 'String', c = True):
    print('a =',a,'; b =', b, '; c =',c)

print_params()
print_params(5)
print_params(7, 'Life is beautiful!')
print_params(9,'Life is Terrible!',False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['The first parameter',121,True]
values_dict = {'a': 17, 'b': True, 'c':'2B || !2B'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 2024]
print_params(*values_list_2, 42)