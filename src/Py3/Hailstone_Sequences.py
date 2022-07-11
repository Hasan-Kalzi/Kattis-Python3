# Hailstone Sequences
# Solution by Hasan Kalzi 05-11-2021
# Link to problem in Kattis: https://open.kattis.com/problems/hailstone2
from sys import stdin, stdout

n = int(stdin.readline())
i = 1
while n > 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
    i += 1
stdout.write(str(i))
