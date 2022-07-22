# R2
# Solution by Hasan Kalzi: 22-07-2022
# Link to the problem: https://open.kattis.com/problems/r2
from sys import stdin, stdout

r1, s = map(int, stdin.readline().split())
stdout.write(str((2*s)-r1))
