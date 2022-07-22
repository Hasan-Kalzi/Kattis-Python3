# Rectangle Area
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/averagecharacter
from sys import stdin, stdout

x1, y1, x2, y2 = map(float, stdin.readline().split())
stdout.write(str(abs(x1 - x2) * abs(y1 - y2)))
