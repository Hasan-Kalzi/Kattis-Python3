# Expected Earnings
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/cutinline
from __future__ import division
from sys import stdin, stdout

n, k, p = map(float, stdin.readline().split())
if k/n <= p:
    stdout.write('spela inte!')
else:
    stdout.write('spela')
