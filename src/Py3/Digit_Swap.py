# Digit Swap
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/digitswap
from sys import stdin, stdout

digit = stdin.readline()
stdout.write(digit[1] + digit[0])
