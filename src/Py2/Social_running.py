# Social running
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/socialrunning
from sys import stdin, stdout, maxsize

distance = []
minimum = maxsize
for _ in range(int(stdin.readline())):
    distance.append(int(stdin.readline()))
for i in range(len(distance)):
    x = distance[i] + (distance[(i - 2) % len(distance)])
    if x < minimum:
        minimum = x
stdout.write(str(minimum))
