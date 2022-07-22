# Prsteni
# Solution by Hasan Kalzi 06-04-2021
# Link to problem in https://open.kattis.com/problems/prsteni
from __future__ import division
from sys import stdin, stdout


def gcd(x, y):
    if x == y:
        return x
    if x > y:
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)


n = int(stdin.readline())
rings = [int(_) for _ in stdin.readline().split()]
for i in range(1, n):
    a = rings[0]
    b = rings[i]
    c = gcd(a, b)
    a /= c
    b /= c
    stdout.write(str(int(a)) + '/' + str(int(b)) + '\n')
