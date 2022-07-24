# Sibice
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sibice
import math
import sys

n, w, h = [int(_) for _ in sys.stdin.readline().split()]
for _ in range(n):
    if int(sys.stdin.readline()) <= math.sqrt((w*w)+(h*h)):
        sys.stdout.write("DA\n")
    else:
        sys.stdout.write("NE\n")
