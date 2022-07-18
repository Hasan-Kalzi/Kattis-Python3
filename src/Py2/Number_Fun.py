# Number Fun
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/numberfun
from __future__ import division
from sys import stdin, stdout
number_of_tests = int(stdin.readline())
for _ in range(number_of_tests):
    first, second, third = map(int, stdin.readline().split())
    if first + second == third:
        stdout.write("Possible\n")
    elif first * second == third:
        stdout.write("Possible\n")
    elif first - second == third or second - first == third:
        stdout.write("Possible\n")
    elif first / second == third or second / first == third:
        stdout.write("Possible\n")
    else:
        stdout.write("Impossible\n")
