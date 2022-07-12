# Hitting the Targets
# Solution by Hasan Kalzi: 10-01-2022
# Link to the problem: https://open.kattis.com/problems/hittingtargets
from sys import stdin, stdout
from math import sqrt


class Circles:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class Recs:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


circles = []
rects = []
for _ in range(int(stdin.readline())):
    target = stdin.readline().split()
    if target[0] == 'rectangle':
        rects.append(Recs(int(target[1]), int(target[2]), int(target[3]), int(target[4])))
    else:
        circles.append(Circles(int(target[1]), int(target[2]), int(target[3])))
for _ in range(int(stdin.readline())):
    x_s, y_s = map(int, stdin.readline().split())
    hits = 0
    for rect in rects:
        if rect.x1 <= x_s <= rect.x2 and rect.y1 <= y_s <= rect.y2:
            hits += 1
    for circle in circles:
        if sqrt(pow(circle.x - x_s, 2) + pow(circle.y - y_s, 2)) <= circle.r:
            hits += 1
    stdout.write(str(hits) + '\n')
