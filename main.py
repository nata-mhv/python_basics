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
s = input()
new_s = ''
for i in range(len(s)):
    selection = s[s.find('h')+1:s.rfind('h')]
    conversion = selection[::-1]
    new_s = s[:s.find('h')+1] + conversion + s[s.rfind('h'):]

print(new_s)