# Zoom
# Solution by Hasan Kalzi 31-03-2022
# Link to problem in Kattis https://open.kattis.com/problems/apaxiaaans
from sys import stdin, stdout

n, x, y = map(int, stdin.readline().split())
for _ in range(n):
    stdout.write(str(int((int(stdin.readline()) * y) / x)) + '\n')
