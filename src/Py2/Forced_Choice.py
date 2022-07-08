# Forced Choice
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/forcedchoice
from sys import stdin, stdout

n, p, s = map(int, stdin.readline().split())
for _ in range(s):
    if p in [int(_) for _ in stdin.readline().split()][1:]:
        stdout.write("KEEP\n")
    else:
        stdout.write("REMOVE\n")
