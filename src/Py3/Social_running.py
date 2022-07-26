# Social running
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/socialrunning
from sys import stdin, stdout

distance, n = [], int(stdin.readline())
minimum = 9223372036854775807
for _ in range(n):
    distance.append(int(stdin.readline()))
for i in range(n):
    x = distance[i] + distance[(i - 2) % len(distance)]
    if x < minimum:
        minimum = x
stdout.write(str(minimum))
