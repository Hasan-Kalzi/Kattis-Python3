# Espresso
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/espresso
from sys import stdin, stdout

n, s = map(int, stdin.readline().split())
curr, refill = s, 0
for i in range(n):
    order = stdin.readline().strip()
    if 'L' in order:
        if curr - (int(order[0]) + 1) < 0:
            curr = s
            refill += 1
        curr -= int(order[0]) + 1
    else:
        if curr - int(order[0]) < 0:
            curr = s
            refill += 1
        curr -= int(order[0])

stdout.write(str(refill))
