# FYI
# Solution by Hasan Kalzi 12-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/fyi
import sys

number = int(sys.stdin.readline())
if 5550000 <= number < 5560000:
    sys.stdout.write('1')
else:
    sys.stdout.write('0')
