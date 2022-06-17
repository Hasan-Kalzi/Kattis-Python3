# Exoplanet Lighthouse
# Solution by Hasan Kalzi 17-06-2022
# Link to problem in Kattis: https://open.kattis.com/problems/exoplanetlighthouse
from __future__ import division
from sys import stdin, stdout
from math import acos
for _ in range(int(stdin.readline())):
    r, h1, h2 = map(float, stdin.readline().split())
    theta1, theta2 = acos(r/(r+(h1/1000))), acos(r/(r+(h2/1000)))
    stdout.write(str(r * (theta1 + theta2)) + '\n')
