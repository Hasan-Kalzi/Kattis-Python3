# Planina
# Solution by Hasan Kalzi 20-07-2022
# Link to problem in Kattis: https://open.kattis.com/problems/planina
from sys import stdin, stdout

iterations = 0
for _ in range(0, int(stdin.readline())):
    iterations *= 2
    iterations += 1
stdout.write(str((iterations + 2) * (iterations + 2)))
