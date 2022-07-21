# Pot
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/pot
from sys import stdin, stdout
from math import floor

result = 0
# after range is the inserted number of lines: int(input())
for _ in range(int(stdin.readline())):
    values = int(stdin.readline())
    result += floor(values/10) ** (values % 10)
stdout.write(str(int(result)))
