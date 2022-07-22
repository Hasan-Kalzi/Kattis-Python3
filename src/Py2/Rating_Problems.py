# Rating Problems
# Solution by Hasan Kalzi 21-06-2021
# # Link to problem in Kattis: https://open.kattis.com/problems/ratingproblems
from __future__ import division

from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
total = 0
for i in range(k):
    total += int(stdin.readline())
stdout.write(str((total - (3 * (n - k)))/n) + " " + str((total + (3 * (n - k)))/n))
