#import random
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(3, 21):
    multiples = []
    pairs = []
    j = 2
    while j <= i:
        if i % j == 0:
            multiples.append(j)
        j += 1
    #print(i, ' - ', multiples)
    for j in multiples:
        k = 1
        while k <= j // 2:
            if k != j - k:
                pairs.append([k, j - k])
            k += 1
        #print(pairs)
    password = ''
    for j in pairs:
        password += str(j[0]) + str(j[1])

    #print(i, ' - ', password)
    print(i, ' - ', multiples, ' - ', pairs, ' - ', password)