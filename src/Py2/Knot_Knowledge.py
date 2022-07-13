# Knot Knowledge
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/knotknowledge
from sys import stdin, stdout

stdin.readline()
stdout.write(str(next(iter(set(stdin.readline().strip().split()) - set(stdin.readline().strip().split())))))
