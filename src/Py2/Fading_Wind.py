# Fading Wind
# Solution by Hasan Kalzi: 28-02-2022
# Link to the problem: https://open.kattis.com/problems/fadingwind
from math import trunc
from sys import stdout,stdin

h,k,v,s = map(int,stdin.readline().split())
distance = 0

while h > 0:
    v = v + s
    v = v - max(1,trunc(v / 10))
    if v >= k:
        h += 1
    if 0 < v < k:
        h -= 1
        if h == 0:
            v = 0
    if v <= 0:
        h,v = 0,0
    distance += v
    if s > 0:
        s -= 1

stdout.write(str(distance))
