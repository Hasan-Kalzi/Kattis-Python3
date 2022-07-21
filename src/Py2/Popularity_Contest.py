# Popularity Contest
# Solution by Hasan Kalzi: 05-01-2022
# Link to the problem: https://open.kattis.com/problems/popularitycontest
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
marketability = list(range(-1, (n * -1) - 1, -1))
if m != 0:
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        marketability[a - 1] += 1
        marketability[b - 1] += 1
for friend in marketability:
    stdout.write(str(friend) + ' ')
