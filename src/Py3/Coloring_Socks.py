# Coloring Socks
# Solution by Hasan Kalzi 06-11-2021
# Link to problem in Kattis: https://open.kattis.com/problems/color
from sys import stdin, stdout

s, c, k = map(int, stdin.readline().split())
colors = sorted([int(_) for _ in stdin.readline().split()])
washers = 1
sock_counter = 0
current_group = [colors[0]]
if len(colors) == 1:
    stdout.write('1')
else:
    for color in colors[1:]:
        if len(current_group) == c:
            washers += 1
            current_group = [color]
        elif color - current_group[0] <= k:
            current_group.append(color)
        else:
            washers += 1
            current_group = [color]
    stdout.write(str(washers))
