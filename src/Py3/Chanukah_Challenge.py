# Chanukah Challenge
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/chanukah
import sys

number_of_tests = int(sys.stdin.readline())

for _ in range(number_of_tests):
    values = [int(x) for x in sys.stdin.readline().split()]
    sys.stdout.write(str(values[0]) + ' ' + str(values[1] + int(values[1] * (values[1] + 1) / 2)) + '\n')
