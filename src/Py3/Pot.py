# Pot
# Solution by Hasan Kalzi 27-09-2020
# Link to problem i Kattis: https://open.kattis.com/problems/pot

import math

result = 0
# after range is the inserted number of lines: int(input())
for _ in range(int(input())):
    values = int(input())
    result += math.floor(values/10) ** (values % 10)
print(result)
