# Different Distances
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/differentdistances
from __future__ import division
from sys import stdin, stdout

while 1:
    coord = [float(_) for _ in stdin.readline().split()]
    if coord[0] == 0:
        break
    else:
        stdout.write(str(pow(pow(abs(coord[0] - coord[2]), coord[4])
                             + pow(abs(coord[1] - coord[3]), coord[4]), 1/coord[4])) + '\n')
