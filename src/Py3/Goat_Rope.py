# Goat Rope
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/goatrope
from math import sqrt
from sys import stdin, stdout

x, y, x1, y1, x2, y2 = map(int, stdin.readline().split())
a, b, c = 0, 0, 0
if x1 <= x <= x2 or y1 <= y <= y2:
    if y < y1:
        a, b, c = 0, 1, -y1
    elif y > y2:
        a, b, c = 0, 1, -y2
    elif x < x1:
        a, b, c = 1, 0, -x1
    else:
        a, b, c = 1, 0, -x2
    stdout.write(str(abs(((a * x) + (b * y) + c) / sqrt((a * a) + (b * b)))))
else:
    stdout.write(str(min([sqrt(pow(x - x1, 2) + pow(y - y1, 2)), sqrt(pow(x - x1, 2) + pow(y - y2, 2)),
                          sqrt(pow(x - x2, 2) + pow(y - y2, 2)), sqrt(pow(x - x2, 2) + pow(y - y1, 2))])))
