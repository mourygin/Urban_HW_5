def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        prime = True
        for i in range(2,n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print('IS PRIME')
        else:
            print('IS NOT PRIME')
        return n
    return wrapper
@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        # print(i)
        if str(i).isnumeric:
            total += i
        else:
            # raise TypeError
            pass
    return total

# sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)