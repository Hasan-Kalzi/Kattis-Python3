# Loo Rolls
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/loorolls
from sys import stdin, stdout

l, n = map(int, stdin.readline().split())
t = l % n
k = 1
while t != 0:
    n -= t
    t = l % n
    k += 1

stdout.write(str(k))
