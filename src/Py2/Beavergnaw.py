# Beavergnaw
# Solution by Hasan Kalzi 22-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/beavergnaw
from __future__ import division
from sys import stdin, stdout
from math import pi

while 1:
    big_d, v = [int(_) for _ in stdin.readline().split()]
    if big_d == 0 and v == 0:
        break
    d3 = big_d * big_d * big_d - (6 * v / pi)
    d = pow(d3, 1 / 3)
    stdout.write("%.9f" % d+'\n')
