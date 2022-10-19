# Planting Trees
# Solution by Hasan Kalzi 19-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/plantingtrees
from sys import stdin, stdout

n, trees = int(stdin.readline()), sorted([int(_) for _ in stdin.readline().split()], reverse=True)
for i in range(n):
    # the day after all grown up -1 and the index -1 = -2
    trees[i] -= n - 2 - i
stdout.write(str(n + max(trees)))
