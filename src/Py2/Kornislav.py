# Kornislav
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/kornislav
from sys import stdin, stdout
values = sorted([int(_) for _ in stdin.readline().split()])

stdout.write(str(values[0] * values[2]))
