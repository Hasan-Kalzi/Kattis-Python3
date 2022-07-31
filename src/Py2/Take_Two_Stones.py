# Take Two Stones
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/twostones
from sys import stdin, stdout
check = int(stdin.readline())
if check % 2 != 0:
    stdout.write("Alice")
else:
    stdout.write("Bob")
