# Joint Jog Jam
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/jointjogjam
from sys import stdin, stdout
from math import sqrt

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, stdin.readline().split())
stdout.write(str(max(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2))))
