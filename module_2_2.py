first = input('Inpun the first number: ')
second = input('Inpun the second number: ')
third = input('Inpun the third number: ')
eq_1 = int(first == second)
eq_2 = int(second == third)
eq_3 = int(first == third)
eq = eq_1 + eq_2 + eq_3
if eq == 1:
    print(2)
else:
    print(eq)

