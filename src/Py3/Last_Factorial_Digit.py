# Last Factorial Digit
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/lastfactorialdigit

import math

for _ in range(int(input())):
    print(math.factorial(int(input())) % 10)
