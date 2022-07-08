# Flying Safely
# Solution by Hasan Kalzi: 10-01-2022
# Link to the problem: https://open.kattis.com/problems/flyingsafely
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    for _ in range(m):
        stdin.readline()
    stdout.write(str(n - 1) + '\n')
