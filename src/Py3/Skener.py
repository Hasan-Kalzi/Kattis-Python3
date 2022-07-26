# Skener
# Solution by Hasan Kalzi 18-03-2021
# Link to problem in https://open.kattis.com/problems/skener
import sys
r, c, zr, zc = map(int, sys.stdin.readline().split())
for _ in range(r):
    s = sys.stdin.readline()
    for _ in range(zr):
        sys.stdout.write(''.join([_ * zc for _ in s[:len(s)-1]])+'\n')
