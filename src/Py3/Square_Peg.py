# Square Peg
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/squarepeg
from sys import stdin, stdout

l, r = map(int, stdin.readline().split())

if l > r * 1.41421356237:
    stdout.write("nope")
else:
    stdout.write("fits")
