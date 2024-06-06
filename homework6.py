my_dict = {'Alex': 1958, 'Liza': 1984, 'Nick': 1985, 'Mike': 2004}
print(my_dict)
print(my_dict.get('Liza'))
print(my_dict.get('Mary','Unknowen name'))
my_dict['Mary'] = 1959
my_dict['Sasha'] = 1989
print(my_dict)
name = 'Alex'
a = my_dict.pop(name)
print(name, ':', a)
print(my_dict)
print('------------')
# my_set = {'Cat', 4, 'Dog', 4, 'Man', 2, 'Ostrich', 2, 'Octopus', 8, 'Woman', 2}
# print(my_set)
my_set = {'Окунь', 250, 'Щука', 1350, 'Плотва', 250, 'Судак', 1350}
print(my_set)
my_set.add('Акула')
my_set.add(350000)
print(my_set.remove(250))
print(my_set)
