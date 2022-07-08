# Forced Choice
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/forcedchoice
import sys

n, p, s = map(int, sys.stdin.readline().split())
for _ in range(s):
    if p in [int(_) for _ in sys.stdin.readline().split()][1:]:
        sys.stdout.write("KEEP\n")
    else:
        sys.stdout.write("REMOVE\n")
