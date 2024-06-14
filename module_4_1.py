from module_4_1_fake_math import divide as fake_divide
from module_4_1_true_math import divide as true_divide

a = 8
b = 0
print(fake_divide(a, b))
print(true_divide(a, b))
print('')

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)