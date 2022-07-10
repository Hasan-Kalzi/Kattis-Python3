# GCVWR
# Solution by Hasan Kalzi 01-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/gcvwr
from sys import stdin, stdout

g, t, n = map(int, stdin.readline().split())
stdout.write(str(int(-sum([int(_) for _ in stdin.readline().split()])+(g-t)*(90/100))))
