# Reverse
# Solution by Hasan Kalzi 18-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/ofugsnuid
import sys

# The first line of input contains the integer n. Then comes a list of n integers, each on its own line.
n = int(sys.stdin.readline())
points = [sys.stdin.readline() for _ in range(n)]
[sys.stdout.write(x) for x in reversed(points)]
