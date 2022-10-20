# Jewelry Box
# Solution by Hasan Kalzi 19-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/jewelrybox
from __future__ import division
from math import sqrt
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    delta = (16 * (x + y) * (x + y)) - (48 * x * y)
    if delta == 0:
        h = (4 * (x + y)) / 24
        stdout.write(str((x - (2 * h)) * (y - (2 * h)) * h) + '\n')
    else:
        h1 = ((4 * (x + y)) + sqrt(delta)) / 24
        h2 = ((4 * (x + y)) - sqrt(delta)) / 24
        vol1 = (x - (2 * h1)) * (y - (2 * h1)) * h1
        vol2 = (x - (2 * h2)) * (y - (2 * h2)) * h2
        if vol1 > vol2:
            stdout.write(str(vol1) + '\n')
        else:
            stdout.write(str(vol2) + '\n')
