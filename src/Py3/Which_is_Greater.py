# Which is Greater
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/whichisgreater
from sys import stdin, stdout

a, b = map(int, stdin.readline().split())
if a > b:
    stdout.write('1')
else:
    stdout.write('0')
