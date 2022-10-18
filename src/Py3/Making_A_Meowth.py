# Making A Meowth
# Solution by Hasan Kalzi 17-10-2022
# Link to problem in https://open.kattis.com/problems/makingameowth
from sys import stdin, stdout

n, p, x, y = map(int, stdin.readline().split())
if n > p:
    stdout.write(str(p * x))
else:
    stdout.write(str((int(p / (n - 1)) * y) + (p * x)))
