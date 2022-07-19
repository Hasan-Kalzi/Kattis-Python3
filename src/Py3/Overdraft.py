# Overdraft
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/overdraft
from sys import stdin, stdout

min_start = [0]
total = 0
for _ in range(int(stdin.readline())):
    total += int(stdin.readline())
    if total < 0:
        min_start.append(total)

stdout.write(str(min(min_start) * -1))
