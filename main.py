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
n = int(input())
s = input()
for i in s:
    decryption = ord(i) - n
    if decryption < 97:
        decryption += 26
    print(chr(decryption), end='')