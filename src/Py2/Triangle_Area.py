# Triangle Area
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/triarea
from __future__ import division
from sys import stdin, stdout


h, b = map(int, stdin.readline().split())
stdout.write(str(h * b / 2))
