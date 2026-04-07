from math import *

#n = int(input())
#max_digit = 0
#min_digit = 9

#while n > 0:
#    current_digit = n % 10

#    max_digit = max(max_digit, current_digit)
#    min_digit = min(min_digit, current_digit)

#    n //= 10

#print("Максимальная цифра равна", max_digit)
#print("Минимальная цифра равна", min_digit)


for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)



