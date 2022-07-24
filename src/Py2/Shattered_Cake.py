# Shattered Cake
# Solution by Hasan Kalzi 25-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/shatteredcake
from __future__ import division
from sys import stdin, stdout
sum_area = 0
w = int(stdin.readline())
# after range is the inserted number of pieces: int(input())
for _ in range(int(stdin.readline())):
    # the width wi and length li of each piece.
    wi, li = map(int, stdin.readline().split())
    sum_area += wi*li
# The output should be the integer L = area/W
stdout.write(str(int(sum_area / w)))
