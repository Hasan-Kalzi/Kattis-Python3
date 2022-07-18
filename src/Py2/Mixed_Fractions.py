# coding=utf-8
# Mixed Fractions
# Solution by Hasan Kalzi 22-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/mixedfractions
from __future__ import division
from sys import stdin, stdout

while 1:
    # Input has one test case per line. Each test case contains two integers in the range [1,231−1]. The first number
    # is the numerator and the second is the denominator. A line containing 0 0 will follow the last test case.
    numerator, denominator = map(int, stdin.readline().split())
    if numerator == 0 and denominator == 0:
        break
    stdout.write(
        str(int(numerator / denominator)) + " " + str(int(numerator % denominator)) + " / " + str(denominator) + "\n")
