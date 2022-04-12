# Beavergnaw
# Solution by Hasan Kalzi 22-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/beavergnaw
from math import pi

while True:
    big_d, v = [int(x) for x in input().split()]
    if big_d == 0 and v == 0:
        break
    d3 = big_d * big_d * big_d - (6 * v / pi)
    d = pow(d3, 1 / 3)
    print("%.9f" % d)
