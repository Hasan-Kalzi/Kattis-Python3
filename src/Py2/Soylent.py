# Soylent
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/soylent
from __future__ import division
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    bottles = int(stdin.readline())/400
    if int(bottles) == bottles:
        stdout.write(str(int(bottles))+'\n')
    else:
        stdout.write(str(int(bottles) + 1) + '\n')
