# Contest Struggles
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/conteststruggles
from __future__ import division
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
d, s = map(int, stdin.readline().split())
average = ((n * d) - (k * s)) / (n - k)
if 0 <= average <= 100:
    stdout.write(str(average))
else:
    stdout.write('impossible')
