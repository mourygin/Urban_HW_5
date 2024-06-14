from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

# print(divide(6,2))
# print(divide(6,0))