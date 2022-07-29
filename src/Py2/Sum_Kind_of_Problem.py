# coding=utf-8
# Sum Kind of Problem
# Solution by Hasan Kalzi 23-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sumkindofproblem
from __future__ import division
from sys import stdin, stdout

# The first line of input contains a single integer P, (1≤P≤10000), which is the number of data sets that follow.
# after range is the inserted number P: int(sys.stdin.readline())
for _ in range(int(stdin.readline())):
    # Each data set consists of a single line of input.
    # It contains the data set number, K, followed by an integer N, (1≤N≤10000).
    k, n = [int(_) for _ in stdin.readline().split()]
    stdout.write(str(k) + " " + str(int((n / 2) * (1 + n))) + " " +
                 str(n * n) + " " +
                 str(n * (n + 1)) + "\n")
