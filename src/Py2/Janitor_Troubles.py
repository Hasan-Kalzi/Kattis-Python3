# Janitor Troubles
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/janitortroubles
from __future__ import division
from math import sqrt
from sys import stdin, stdout

# The input consists of a single line with four positive integers, the four side lengths s1, s2, s3, and s4.
s1, s2, s3, s4 = map(int, stdin.readline().split())
semi_perimeter = (s1 + s2 + s3 + s4) / 2
stdout.write(str(sqrt((semi_perimeter - s1) * (semi_perimeter - s2)
                      * (semi_perimeter - s3) * (semi_perimeter - s4))))
